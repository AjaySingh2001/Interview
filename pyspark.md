# Pyspark

* PySpark is the Python API for Apache Spark, a powerful framework designed for distributed data processing. If you’ve ever worked with large datasets and found your programs running slowly, PySpark might be the solution you’ve been searching for. It allows you to process massive datasets across multiple computers at the same time, meaning your programs can handle more data in less time.

So, think of PySpark as:

> **Pandas for Big Data**, powered by many computers.


## Why spark is fast?
- Spark keeps most data in RAM, making it much faster.
- Spark splits data into small chunks and processes them simultaneously across multiple computers
- Spark’s DAG (Directed Acyclic Graph) engine automatically finds the best way to run your operations, reducing unnecessary steps.

> stores data in memory + works in parallel + plans smartly.


# Components of spark:
Apache Spark has **five main components**:

1. ⚙️ **Spark Core** –
The foundation of Spark. Handles basic functions like **task scheduling, memory management, fault recovery**, and **interacting with storage**.

2. 🧮 **Spark SQL** –
Used for working with **structured data** using **SQL queries** or **DataFrames** (like tables).

3. 🔥 **Spark Streaming** –
Processes **real-time data streams**, e.g., live logs or sensor data.

4. 🤖 **MLlib (Machine Learning Library)** –
Provides ready-made **machine learning algorithms** like classification, regression, clustering, etc.

5. 🌐 **GraphX** –
Used for **graph processing**, such as analysing social networks or connections.

✅ **In short:**

> Spark Core (base) + SQL + Streaming + MLlib + GraphX = Apache Spark.

# Architecture

![Architecture](./architecture.png)

---

### 🔷 **1. Driver Program**

* The **main Python application** you write.
* It creates the **SparkContext** (entry point to Spark).
* The driver sends tasks to the cluster and collects results.

---

### 🔷 **2. Cluster Manager**

* Allocates **resources (CPU, memory)** to run your application.
* Examples: **Standalone**, **YARN**, **Mesos**, or **Kubernetes**.

---

### 🔷 **3. Executors**

* Run on **worker nodes**.
* Each executor executes a part of the task and stores data in memory.
* They report results back to the driver.

---

### 🔷 **4. Worker Nodes**

* Machines in the cluster that actually **perform the computation**.

---

### 🔷 **5. RDD / DataFrame**

* The **core data structures** in PySpark used for distributed data processing.

---

**In short:**

> PySpark architecture = **Driver Program** (controls) + **Cluster Manager** (allocates) + **Executors on Worker Nodes** (execute).

It follows a **master–slave architecture**, where the **driver is the master** and **executors are the slaves** performing the actual work.


## Start Session

```python
    from pyspark.sql import SparkSession

    spark = SparkSession.builder \
        .appName("MyApp") \
        .getOrCreate()

    print(spark)          # Should print SparkSession object
    print(spark.version)  # Should print Spark version, e.g., 3.5.0
```


# Create Dataframe


```python
    Name = [("A", 20), ("B", 30), ("C", 40)]
    Column = ["Name", "Age"]

    df = spark.CreateDataFrame(Name, Columns)


    # Visualize using matplotlib

    pdf = df.to_pandas()

    plt.figure(figsize = (6,4))
    plt.bar(pdf["Name"], pdf["Age"])
    plt.xlabel("Name")
    plt.ylabel("Age")

```

## printSchema()

A method that prints the schema in a tree format.

- print(df.printSchema())

## columns

columns → Attribute (not a function) that returns a Python list of column names.

- df.columns

## Count()
count() → method that returns an integer representing the number of rows.

df.count()

## describe

- df.describe() → Computes summary statistics.
- show() → Displays the results in a tabular format.



## Column methods

1. Selection & Access

    1. df["colname"]
        - What it does: Returns a Column object representing that column.
        - Type: Column
        - Usage: For transformations, filters, or expressions, not to display data directly.

        ```python 
            Column<'Name'>

    2. df.select("colname")
        - What it does: Returns a DataFrame with only the specified column(s).
        - Type: DataFrame
        - Usage: When you want to view or work with a subset of columns.

        ```python
            output: DataFrame[Age: bigint]

    3. col("colname") from pyspark.sql.functions
        - What it does: Returns a Column object.
        - Type: Column
        - Usage: Useful in expressions, select, withColumn, or when column name is a string variable.

        ```python
            output: DataFrame[Name: string]


2. Add or modify column

> Note: Spark never changes the original DataFrame.

1. withColumn: Use withColumn() (the PySpark way to add or modify a column):

# Read csv

- spark.read.format('csv').option('inferSchema', True).load("BigMartSales.csv")

1. spark.read
    - Starts the DataFrameReader.
    - Used to read data from different sources — CSV, JSON, Parquet, etc.

2. .format('csv')
    - Specifies the file format to read.
    - You could replace 'csv' with 'json', 'parquet', 'orc', etc.

3. .option('inferSchema', True)

    - Tells Spark to automatically detect the data type of each column.
        Example:
        - "25" → integer
        - "Ajay" → string
    - If not used, Spark treats all columns as strings by default.

4. .load("BigMartSales.csv")
    - Loads the file from the given path into a DataFrame.
    - Spark reads the file in parallel across multiple cores.


# Read JSON

spark.read.format("json").load("path to file")

.option("multiline", True): Allow us to devine the data format inside the json. default: multiline= False





## Access Column

1. Accessing Columns

    ```python
    df.select("name").show()
    ```

2. Access multiple columns

    ```python
    df.select("name", "age").show()
    ```

3. Column object (for expressions)

    ```python
    from pyspark.sql.functions import col, upper

    df.select(upper(col("name")), col("age")+100)
    ```

## Access Rows

1. Show first N rows

    ```python
    df.show(5)

2. Take first N rows as list

    ```python
    df.take(3)  # returns list of Row objects


3. Collect all rows (be careful for large DF!)

    ```python
    df.collect()  # returns list of Row objects

4. first row

    ```python
    df.first()

5. filter rows

    ```python
    df.filter(df.age > 10).show()


    # or we can use

    df.where(col("age")>10).show()


## Adding/Manipulating Columns

1. Add new column


    ```python
    df.withColumn("age_plus+5", col("age")+5).show()


- What it does:

    - df → your original DataFrame (like a table).

    - .withColumn("age_plus_5", ...) → creates a new column in the DataFrame.

    - "age_plus_5" → name of the new column.

    - col("age") + 5 → calculation for the new column: take the existing column age and add 5 to it.

>Important: PySpark DataFrames are immutable, which means the original df does NOT change. You always create a new DataFrame when you transform it.

2. Rename Column

    ```python
    df3 = df2.withColumnRenamed("age_plus+5", "5_added")

3. Drop column

    ```python
    df4 = df3.drop("5_added")


4. Modify column

    ```python
    df2 = df2.withColumn("age", col("age") + 1)


## Access column values (like Pandas)


df.select("column").collect()[0][0]

## Selecting distinct / unique values

df.select("name").distinct().show()
