Def: RDD(Resilient Distributed Dataset)
RDD is a distributed collection of data that can be processed in parallel acreoss multipole computers.

Procedure:
Let's break the RDD name:
Step 1: Resilent
        Resilient means fault-tolerant.
        If one machine fails, Spark can recover the data.
Step 2: Distributed:
        Distributed means data is divided and stored across multiple computers.
Step 3: Dataset:
        Dataset means a collection of data.
        Example : [1, 2, 3, 4] ---> This is a dataset

-----Code:
# Import SparkSession
from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("RDDExample") \
    .getOrCreate()

# Create Python list
numbers = [10, 20, 30, 40, 50]

# Convert Python list into RDD
rdd = spark.sparkContext.parallelize(numbers)

# Display RDD data
print(rdd.collect())


Explanation:
Step 1: #Import SparkSession

Step 2: #Create Spark Session
        Starts the spark application

Step 3: # Create Python list
        Create python list

Step 4: # Convert Python list into RDD
        Converts the list into an RDD.
        Spark can distribute this data.

Step 5: # Display RDD data
        Collect data from executors and display it.
