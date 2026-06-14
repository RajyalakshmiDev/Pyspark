Big Data:
-----------
Big Data is a large volume of data that cannot be processed efficiently using traditional tools and methods.

--- Process:
Normally, We can store and analyze small amounts of data using Excel, sql or python.
However companies like Amazon, netflix and google generates millions of records every day.
Examples:
-> Customer orders 
-> Video views
-> Online Transaction 
-> Search history

When the data becomes too large to handle using traditional tools. it is called Big data.


PySpark:
-----------
PySpark is the Python API for Apache Spark that is used to process and analyze large ampounts of data quickly and efficiently.

--- Process:
PySpark allows us to use python with Apache Spark.
Apache Spark is a powerful framework designed to process huge amounts of data very quickly
instead of using only one computer, Spark can divide the work across multiple computers and process data in parallel.
This makes data processing much faster.
Example:
Imagine Amazon has 10 million customer orders
The Company wants to find:
which product sold the most?
which city placed the highest number of orders?
processing this data with normal tools can be slow
PySpark helps process this huge amount of data quickly

Example Code:
-------------
# Import SparkSession from PySpark
from pyspark.sql import SparkSession

# Create a Spark Session
spark = SparkSession.builder \
    .appName("Day1_PySpark") \
    .getOrCreate()

# Print a message
print("Hello PySpark")

--Output:
Hello PySpark



  
  

