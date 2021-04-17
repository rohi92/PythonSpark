from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
import pandas as pd
spark_config = SparkConf()
sc=SparkContext(conf=spark_config)
spark=SparkSession.builder.appName("Myfirst").getOrCreate()
stop_Timesstop_times=spark.read.format("csv").\
option("header","True").option("inferschema","True").\
load("oci://Python_Spark_Code@idv3oy4sejuc/Stop_Timesstop_times.txt")
tripstrips=spark.read.format("csv").\
option("header","True").option("inferschema","True").\
load("oci://Python_Spark_Code@idv3oy4sejuc/tripstrips.txt")
#sample_csv.write.format("orc").save("oci://Python_Spark_Code@idv3oy4sejuc/sample_df.orc")
stop_Timesstop_times.createTempView('stop_times')
tripstrips.createTempView('trips')
spark.sql("SET spark.sql.autoBroadcastJoinThreshold=-1")
final_query=spark.sql("SELECT a.route_id,a.service_id,b.trip_id from trips a LEFT JOIN stop_times b ON a.trip_id=b.trip_id")
final_query=final_query.repartition(1)
final_query.write.format("orc").save("oci://Python_Spark_Code@idv3oy4sejuc/final_query1.orc")
