from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
import pandas as pd
#loading files
def df_load_data(format,header,inferschema,path):
 if format=="csv":
     df1 = spark.read.format(format).option("header",header).option("inferschema",inferschema).load(path)
 elif format=="parquet":
     df1 = spark.read.parquet(path)
 elif format=="avro":
     df1=spark.read.format(format).load(path)
 elif format=="text":
     df1 = spark.read.text(path)
     return df1
#num of partitions
def get_num_partitions(df):
 num=df.rdd.getNumPartitions()
 return num
def transformation_shuffle(df1,df2):
 spark.sql("SET spark.sql.autoBroadcastJoinThreshold=-1")
 final_query = spark.sql("SELECT a.stop_id,a.stop_name,a.stop_lat count from stops a JOIN stops_times b ON a.stop_id=b.trip_id ")
 return final_query

def transformation_broadcast(df1,df2):
 stops.createTempView("stops")
 stops_times.createTempView("stops_times")
 final_query = spark.sql(
 "SELECT a.stop_id,a.stop_name,a.stop_lat count from stops a JOIN stops_times b ON a.stop_id=b.trip_id")
 return final_query

if __name__=="__main__":
 spark_config = SparkConf()
 sc = SparkContext(conf=spark_config)
 spark =SparkSession.builder.appName("Myfirst").getOrCreate()
 #load stops csv file into a df
 stops=df_load_data("csv",True,True,r"Stops.csv")
 stops_times = df_load_data("csv", True, True, r"stop_times.csv")
 #post load get the num of partitions
 print("Partitions before joins: ",get_num_partitions(stops),get_num_partitions(stops_times))
 #broadcast join
 broadcast_df=transformation_broadcast(stops, stops_times)
 print("Partitions after joins: ", get_num_partitions(stops), get_num_partitions(stops_times),get_num_partitions(broadcast_df))
 #shuffle join
 resultant_df=transformation_shuffle(stops,stops_times)
 #post shuffle the count of Partitions increases to 200 shuffle join was used
 print("Partitions after shuffle joins: ", get_num_partitions(stops), get_num_partitions(stops_times),get_num_partitions(resultant_df))


