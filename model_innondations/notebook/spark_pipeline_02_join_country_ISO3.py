from pyspark import SparkContext

# from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.types import FloatType  # Spark Date type

# from pyspark.sql.functions import to_timestamp
import pyspark.sql.functions as F

import shutil

# import pandas as pd

DATASET_FOLDER = "/media/data-nvme/dev/datasets/WorldBank/"
SPARK_MASTER = "spark://192.168.0.9:7077"
APP_NAME = "Compute moving feature on NOAA dataset"

input_folder = DATASET_FOLDER + "daily_rain_by_country"
output = DATASET_FOLDER + "daily_rain_by_country_ISO3"
country_codes = DATASET_FOLDER + "country-codes.csv"

print("Create Spark session")
spark = (
    SparkSession.builder.master(SPARK_MASTER)
    .appName(APP_NAME)
    .config("spark.driver.memory", "20g")
    .getOrCreate()
)

print("Load NOAA data")
df = (
    spark.read.format("csv")
    .option("header", False)
    .option("multiLine", True)
    .load(input_folder)
    .toDF(
        "date",
        "country_ISO2",
        "avg_rain",
        "sum_rain",
        "max_rain",
        "stddev_rain",
        "station_count",
    )
)
df = df.dropna()
df.createOrReplaceTempView("noaa")

##############################################################################
####### Join country code to have ISO3 instead of FIPS
print("Load table of country code")
df_country_codes = (
    spark.read.format("csv")
    .option("header", True)
    .option("multiLine", True)
    .load(country_codes)
)
df_country_codes.createOrReplaceTempView("country_codes")

df.createOrReplaceTempView("noaa")
print("Join NOAA and countries")
df_full = spark.sql(
    """SELECT country_ISO2, country_codes.`ISO3166-1-Alpha-3` as country_ISO3, date, avg_rain, sum_rain, max_rain, stddev_rain, station_count 
                            FROM noaa LEFT JOIN country_codes ON noaa.country_ISO2=country_codes.FIPS
                            """
)

print("Manualy setting Serbia to SRB")
df_full = df_full.withColumn(
    "country_ISO3",
    F.when(F.col("country_ISO2") == "RI", "SRB").otherwise(F.col("country_ISO3")),
)
df_full.createOrReplaceTempView("noaa")

print("Remove timestamp")
df_full = df_full.drop("country_ISO2")

print("Saving to disk...")
shutil.rmtree(output, ignore_errors=True)
df_full.write.csv(output)
print(df_full.columns)
header = ", ".join(df_full.columns)
print(header)
print("End Spark session")
spark.stop()
