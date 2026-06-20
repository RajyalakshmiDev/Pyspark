Project Name:
Student marks collection system

Ojective:
Store student marks and collect them using spark.

Code:
---------
# Import SparkSession
from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("StudentMarksProject") \
    .getOrCreate()

# Student marks
marks = [75, 80, 90, 65, 88]

# Convert marks into RDD
marks_rdd = spark.sparkContext.parallelize(marks)

# Collect marks from executors
final_marks = marks_rdd.collect()

# Print marks
print("Student Marks:", final_marks)

-----Output:
Student Marks: [75, 80, 90, 65, 88]


Explanation:
-------------
Step 1: # Import Sparksession

Step 2: # Create Spark Session
        Starts the spark application

Step 3: # Student marks
        Stores student marks

Step 4: # Convert marks into RDD
        Converts the python list into an RDD
        spark can now process this data

Step 5: # Collect marks from executors
        Collect the data back to the driver

Step 6: # Print marks
        Display the marks




