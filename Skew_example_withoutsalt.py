from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
import pandas as pd
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
spark_config = SparkConf()
sc=SparkContext(conf=spark_config)
spark=SparkSession.builder.appName("Myfirst").getOrCreate()
biglog=sc.textFile("oci://Python_Spark_Code@idv3oy4sejuc/bigLogNewText.txt")
schema='string'
biglog1=biglog.toDF(schema)
biglog1.createTempView('tab1')
biglog2=spark.sql("select substr(value,1,instr(value,':')-1) as value  from tab1")
biglog2.createTempView('tab2')
biglog3=spark.sql("select value,count(value) from tab2 group by value")
biglog3.show()