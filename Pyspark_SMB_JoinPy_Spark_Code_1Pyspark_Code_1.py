from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
import pandas as pd
spark_config = SparkConf()
sc=SparkContext(conf=spark_config)
spark=SparkSession.builder.appName("Myfirst").getOrCreate()
biglog=sc.textFile("oci://Python_Spark_Code@idv3oy4sejuc/Big_log_TextbigLogNew.txt")
biglog=biglog.toDF()
#sample_csv.write.format("orc").save("oci://Python_Spark_Code@idv3oy4sejuc/sample_df.orc")
biglog.createTempView('biglog')
print("The Default partitions of 1.3GB File are set as : ",biglog.rdd.getNumPartitions())
biglog1=spark.sql("select substr(col1,0,instr(col1,':')-1) as status,substr(col1,instr(col1,':')+1) as date from biglog")
print("The Default partitions of 1.3GB File are set as : ",biglog1.rdd.getNumPartitions())
biglog2=spark.sql("select count(status), status  from biglog group by status")
print("The Default partitions of 1.3GB File are set as : ",biglog2.rdd.getNumPartitions())

