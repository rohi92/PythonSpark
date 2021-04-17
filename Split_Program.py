from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
import pandas as pd
spark_config = SparkConf()
sc=SparkContext(conf=spark_config)
spark=SparkSession.builder.appName("Myfirst").getOrCreate()
biglog=sc.textFile("oci://Python_Spark_Code@idv3oy4sejuc/Big_log_TextbigLogNew.txt")
biglog=biglog.zipWithIndex()
schema='string'
biglog1=biglog.toDF(schema)
biglog.take(4)
biglog1.show()
