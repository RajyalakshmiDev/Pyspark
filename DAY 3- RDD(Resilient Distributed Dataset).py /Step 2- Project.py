Project Name: 
---------------
Employee Salary Collection System

Objective:
--------------
Store employee salaries in an RDD and display them.

Code:
-------------
# Import SparkSession
from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("SalaryProject") \
    .getOrCreate()

# Employee salaries
salaries = [10000, 20000, 30000, 40000, 50000]

# Convert list into RDD
salary_rdd = spark.sparkContext.parallelize(salaries)

# Collect data
result = salary_rdd.collect()

# Print result
print("Employee Salaries:", result)



 ------Output:
      

Employee salaries: [10000, 20000, 30000, 40000, 50000]

------Explanation:
Step 1: # Create Salary List 
        salaries = [25000, 35000, 45000, 55000]
        Stores employee salaries.
Step 2: # Convert to RDD 
        salary_rdd = spark.sparkContext.parallelize(salaries)
        Creates an RDD from the list.
Step 3: # Collect Data
        result = salary_rdd.collect()
        Collect Data
Step 4: # Print Result
        print("Employee Salaries:", result)
        Displays the salaries.
        
       
          

      
