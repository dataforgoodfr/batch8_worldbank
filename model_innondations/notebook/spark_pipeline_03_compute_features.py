from pyspark import SparkContext
#from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql.types import FloatType # Spark Date type
#from pyspark.sql.functions import to_timestamp
import pyspark.sql.functions as F

import shutil
#import pandas as pd

DATASET_FOLDER = '/media/data-nvme/dev/datasets/WorldBank/'
SPARK_MASTER = 'spark://192.168.0.9:7077'
APP_NAME = 'Compute moving feature on NOAA dataset'

input_folder = DATASET_FOLDER + 'daily_rain_by_country_ISO3'
output = DATASET_FOLDER + 'daily_rain_by_country_feature'

print('Create Spark session')
spark = SparkSession.builder.master(SPARK_MASTER).appName(APP_NAME).config("spark.driver.memory", "20g").getOrCreate()

print('Load NOAA data')
df = spark.read.format('csv').option('header',False).option('multiLine', True).load(input_folder)\
    .toDF('country_ISO3', 'date', 'avg_rain', 'sum_rain', 'max_rain', 'stddev_rain', 'station_count')
df=df.dropna()
df.createOrReplaceTempView("noaa")


##############################################################################
###### Cast Type
print('Cast string to float')
df_full = df.withColumn("avg_rain", df["avg_rain"].cast(FloatType()))\
    .withColumn("sum_rain", df["sum_rain"].cast(FloatType())) \
    .withColumn("max_rain", df["max_rain"].cast(FloatType()))

print('Cast date to timestamp')
df_full = df_full.withColumn("date_with_time", F.to_timestamp(df_full.date, 'yyyy-MM-dd'))

print('Helper function to compute number of second in a day')
days = lambda d:d*24*60*60

#############################################################################
##### Compute new features
# Thanks to  https://kevinvecmanis.io/pyspark/data%20science/python/2019/06/02/SPX-Analysis-With-PySpark.html
print('Define a window to make computation')
windowSpec = Window.partitionBy(['country_ISO3']).orderBy(F.col("date_with_time").cast("long"))

df_rolling = df_full
print('Compute moving average and sum')
for d in [5,10,20]:# ,30,60
    # Moving Sum of rain
    df_rolling = df_rolling.withColumn('last_'+str(d)+'_days_sum', F.sum("avg_rain").over(windowSpec.rangeBetween(-days(d), 0)))
    # Moving average of rain
    df_rolling = df_rolling.withColumn('last_'+str(d)+'_days_avg', F.avg("avg_rain").over(windowSpec.rangeBetween(-days(d), 0)))
    # Moving max of rain
    df_rolling = df_rolling.withColumn('last_'+str(d)+'_days_max', F.max("max_rain").over(windowSpec.rangeBetween(-days(d), 0)))

# print('Compute World Bank feature')
# # Number of Days per month with Rainfall > 20mm 
# df_rolling = df_rolling.withColumn('days_per_month_with_rainfall_20mm', F.sum("avg_rain").over(windowSpec.rangeBetween(-days(d), 0)))

# # Number of Days with Rainfall > 50mm : Average count of days per month or year with at least 50mm of daily rainfall.
# df_rolling = df_rolling.withColumn('days_per_month_with_rainfall_50mm', F.sum("avg_rain").over(windowSpec.rangeBetween(-days(d), 0)))

# # Rainfall Amount from Very Wet Days :(Percentage)  Monthly or annual sum of rainfall when the daily
# # precipitation rate exceeds the local 95th percentile of daily precipitation intensity.
# # TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO TODO
# #df_rolling = df_rolling.withColumn('pct_monthly_sum_of_rainfall_50mm', 'todo')

# # Largest Single Day Rainfall : (mm) Monthly or annual average of the largest daily rainfall amount
# df_rolling = df_rolling.withColumn('max_Daily_month_mm', F.max("max_rain").over(windowSpec.rangeBetween(-days(30), 0)))

# # Largest 5-day Cumulative Rainfall : (mm) Monthly or annual average of the largest 5-day consecutive rainfall amount.
# df_rolling = df_rolling.withColumn('max_5day_month_mm', F.max("last_5_days_sum").over(windowSpec.rangeBetween(-days(30), 0)))

# # Maximum Daily Rainfall (10-yr RL) : (mm) Statistical 10-yr return level of the largest daily rainfall event.
# df_rolling = df_rolling.withColumn('max_Daily_10y_mm', F.max("max_rain").over(windowSpec.rangeBetween(-days(30*12*10), 0)))

# # Maximum 5-day Rainfall (10-yr RL) : (mm) Statistical 10-yr return level of the largest 5-day consecutive rainfall sum.
# df_rolling = df_rolling.withColumn('max_5day_25y_mm', F.max("last_5_days_sum").over(windowSpec.rangeBetween(-days(30*12*10), 0)))

# # Maximum Daily Rainfall (25-yr RL) : (mm) Statistical 25-yr return level of the largest daily rainfall event.
# df_rolling = df_rolling.withColumn('max_daily_25y_mm', F.max("max_rain").over(windowSpec.rangeBetween(-days(30*12*25), 0)))

# # Maximum 5-day Rainfall (25-yr RL) : (mm) Statistical 25-yr return level of the largest 5-day consecutive rainfall sum.
# df_rolling = df_rolling.withColumn('max_5day_25y_mm', F.max("last_5_days_sum").over(windowSpec.rangeBetween(-days(30*12*25), 0)))

# # Maximum Monthly Rainfall (10-yr RL) : (mm) Statistical 10-yr return level of the largest monthly rainfall sum
# df_rolling = df_rolling.withColumn('max_month_10y_mm', F.max("max_rain").over(windowSpec.rangeBetween(-days(30*12*10), 0)))

# # Maximum Monthly Rainfall (25-yr RL) : (mm)
# df_rolling = df_rolling.withColumn('max_month_25y_mm', F.max("last_30_days_sum").over(windowSpec.rangeBetween(-days(30*12*25), 0)))

print('Remove timestamp')
df_rolling = df_rolling.drop('date_with_time')

print('Saving to disk...')
shutil.rmtree(output, ignore_errors=True)
df_rolling.write.csv(output, header=True)
print(df_rolling.columns)
header = ', '.join(df_rolling.columns)
print(header)
print('End Spark session')
spark.stop()
