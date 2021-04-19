
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
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
def transformation(df1):
 df2 =spark.sql("select substr(value,0,instr(value,':')-1) as stat,substr(value,instr(value,':')+1) as date from log")
 df3=salting(df2)
 df3=df3.withColumn("effective",concat("salt_key","stat"))
 df3.createTempView("log1")
 df4 = spark.sql("select count( stat),stat from log1 group by stat")

 return df4

def salting(df):
 df = df.withColumn("key", monotonically_increasing_id())
 df.createTempView("log2")



 biglog4 = spark.sql(
 "select case when key between 0 and 10000000 then '1'||stat when key between 10000001 and 20000000 then '2'||stat"
 " when key between 20000001 and 30000000 then '3'||stat when key between 30000001"
 " and 40000000 then '4'||stat end as salt_key, stat from log2")
 return biglog4

if __name__=="__main__":
 spark_config = SparkConf()
 sc = SparkContext(conf=spark_config)
 spark =SparkSession.builder.appName("Myfirst").getOrCreate()
 #load stops csv file into a df
 biglog=df_load_data("text",True,True,"bigLogNew.txt")
 biglog.createTempView("log")
 #get the count of stat
 df3=transformation(biglog)

 df3.show()






