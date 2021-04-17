from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
import pandas as pd
spark_config = SparkConf()
sc=SparkContext(conf=spark_config)
spark=SparkSession.builder.appName("Myfirst").getOrCreate()
biglog=sc.textFile("oci://Python_Spark_Code@idv3oy4sejuc/Big_log_TextbigLogNew.txt")
#sample_csv.write.format("orc").save("oci://Python_Spark_Code@idv3oy4sejuc/sample_df.orc")
schema='string'
biglog1=biglog.toDF(schema)
biglog=biglog.zipWithIndex()
biglog1.createTempView('log1')
biglog1=spark.sql("select _1 as Value,_2 as key from log1")
print("Total Number of before instr Partitions ",biglog1.rdd.getNumPartitions())
print("Total Number of before instr Partitions ",biglog1.rdd.getNumPartitions())
biglog2=spark.sql("select substr(value,0,instr(value,':')-1) as status, substr(value,instr(value,':')+1) as date,key from log1")
biglog2.createTempView('log2')
biglog4=spark.sql("select case when key between 0 and  40000000 then  '1'||status when key between 4000001 and 8000000 then '2'||status when key between 8000001 and 1200000 then '3'||status  when key between 1200001 and 1600000 then '4'||status  when key between 1600001 and 3200000 then '5'||status  else '6'||status end as salt_key, status from log3")
biglog4.createTempView('log4')
biglog4=spark.sql("select salt_key, count(status) as count from log4 group by salt_key")
print("Total Number of before group by Partitions ",biglog1.rdd.getNumPartitions())
#b=spark.sql("select substr(value,0,instr(value,':')-1) as status, substr(value,instr(value,':')+1)"
#           " as date,row_number() over(partition by substr(value,0,instr(value,':')-1) order by substr(value,instr(value,':')+1) ) as stat_num from tab")
#b.createTempView('tabc')
#c=spark.sql("select status,date,case when stat_num <50000 then 42 else stat_num%50000 end as hash_func from tabc")
#c.createTempView("tabd")
#d=spark.sql("select status,date,concat(status,hash_func) as salted_key from tabd")
#d.createTempView("tabe")
#e=spark.sql("select count(salted_key),salted_key from tabe group by salted_key")
#e.show()
#e.rdd.getNumPartitions()

b=spark.sql("select count(status), status from tab1 group by status")
print("Total Number of before instr Partitions ",b.rdd.getNumPartitions())
biglog4.repartition(1)
b.write.format("csv").save("oci://Python_Spark_Code@idv3oy4sejuc/sample_df.csv")

