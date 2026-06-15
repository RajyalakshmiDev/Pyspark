Project Name:
Employee Information System

Objective: 
Storing employee names and displaying the total employee count.

Code:
# Import SparkSession
from pyspark.sql import SparkSession
# Create Spark Session
spark = SparkSession.builder \
    .appName("Employee_Project") \
    .getOrCreate()
# Employee list
employees = ["Raji", "Siri", "Tulasi", "Gayathri"]
# Display employee names
print("Employees:", employees)
# Display total employee count
print("Total Employees:", len(employees))

---Output:
Employees: ['Raji', 'Siri', 'Tulasi', 'Gayathri']
Total Employees: 4


----Code Explanation:
# Step 1: Import SparkSession
This line imports SparkSession from the PySpark library
SparkSession is the entry point for working with PySpark
without SparkSession, we cannot start any PySpark application.

#Step 2: Create Spark Session
This code creates a spark session
builder -> Starts the process of creating a Spark Session
.appName("Employee_Project")-> Gives a name to the application
.getOrCreate() -> Create new Spark Session if one doesn't exist. if session already exists, it uses the existing one.

#Step 3: Employee list
This line creates a python list called "employees".
The list contains four employee names:
.Raji
.Siri
.Tulasi
.Gayathri

#Step 4: Display employee names
 The print() function displays the employee list on the screen

#Step 5: Display total employee count
The len() function counts the number of items in the list.

