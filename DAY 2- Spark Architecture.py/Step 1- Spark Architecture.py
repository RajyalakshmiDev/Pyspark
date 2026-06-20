Definition:
------------------
Spark Architecture is the structure that explains how apache spark processes data using multiple computers and components.

Procedure:
-----------------
Spark does not process data alone.
it uses different componenets that work together as a team.
The three main components are :
1. Driver
2. Executer
3. cluster
Think of spark as a company
. Driver = Manager
. Executer = Employees
. Cluster = Office
The Manager assign work to employees. Employees complete the work and send the results back to the manager.


Code:
--------
# Import SparkSession
from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("ArchitectureExample") \
    .getOrCreate()

# Create sample data
numbers = [1, 2, 3, 4, 5]

# Convert list into RDD
rdd = spark.sparkContext.parallelize(numbers)

# Collect data back to Driver
result = rdd.collect()

# Print result
print(result)

----Output:
[1, 2, 3, 4, 5]    
      




      
