from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

import shutil

DATASET_FOLDER = '/media/data-nvme/dev/datasets/WorldBank/'
SPARK_MASTER = 'spark://192.168.0.9:7077'
APP_NAME = 'Group daily rain by Country'

# spark-submit --master spark://192.168.0.9:7077 --executor-memory 26G --name groupbycountry /media/data-nvme/dev/src/batch8_worldbank/model_innondations/pipeline/spark_pipeline.py

noaa_csv_path = DATASET_FOLDER + '/noaa/*.csv'
#noaa_csv_path = DATASET_FOLDER + 'noaa/ASN*.csv'
output = DATASET_FOLDER + 'daily_rain_by_country'

# Create Spark session
spark = SparkSession.builder.master(SPARK_MASTER).appName(APP_NAME).getOrCreate()
# Convert list to data frame
df = spark.read.format('csv').option('header',True).option('multiLine', True).load(noaa_csv_path)
df_rain = df[["STATION","DATE","LATITUDE","LONGITUDE","ELEVATION","NAME","PRCP","PRCP_ATTRIBUTES"]]

# Extract country code
df_rain = df_rain.withColumn('COUNTRY',  F.col('NAME').substr(F.length('NAME')-1, F.length('NAME')))

# Register the DataFrame as a SQL temporary view
df_rain.createOrReplaceTempView("noaa")
sqlDF = spark.sql("SELECT DATE, COUNTRY, ceil(100 * avg(PRCP))/100 as avg_PRCP, ceil(100 * sum(PRCP))/100 as sum_PRCP, max(PRCP) as max_PRCP, ceil(100 * stddev(PRCP))/100 as stddev_PRCP, count(PRCP) as count_PRCP FROM noaa GROUP BY DATE, COUNTRY;")

shutil.rmtree(output, ignore_errors=True)
#sqlDF.repartition(1).write.csv(output)
sqlDF.write.csv(output)
print(sqlDF.columns)