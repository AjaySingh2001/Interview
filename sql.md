# What is SQL?

- SQL stands for Structured Query Language.
- It is the standard language used to interact with relational databases (RDBMS).
- SQL is used to create, read, update, and delete data — often abbreviated as CRUD.

## Key Features of SQL

1. Structured & Relational
    - Data is stored in tables (rows and columns).
    - Tables can be related using primary keys and foreign keys.

2. Schema-based
    - Each table has a fixed schema (column names and data types).
    - Example: a Users table might have id (int), name (varchar), email (varchar).

3. ACID Compliance
    - SQL databases follow ACID properties:
    - Atomicity – all or nothing transactions
    - Consistency – data stays valid after a transaction
    - Isolation – transactions don’t interfere
    - Durability – committed transactions are saved permanently

### Popular SQL Databases

- MySQL – widely used, free, easy to deploy
- PostgreSQL – advanced features, ACID compliant, supports JSON
- Oracle – enterprise-grade, very robust
- SQL Server – Microsoft database

# What is NoSQL?

- NoSQL stands for “Not Only SQL”.
- It’s a type of database that is non-relational, meaning it does not use tables with fixed schemas like SQL databases.
- Data is stored in flexible formats:
    - Key-Value (Redis, DynamoDB)
    - Document (MongoDB, CouchDB)
    - Column-Family (Cassandra, HBase)
    - Graph (Neo4j)

## Why use NoSQL?

1. Flexible Schema
    - You can store unstructured or semi-structured data.
    - Example: JSON documents for user profiles with different fields.

2. Horizontal Scalability
    - NoSQL databases are designed to scale out by adding more servers.
    - Great for big data and high traffic applications.

3. High Performance for Large Data
    - Optimized for fast reads/writes for large datasets.
    - Example: social media feeds, logs, IoT sensor data.

4. Handling Rapidly Changing Data
    - Schemas can evolve without downtime.
    - Useful for agile development, apps with dynamic data models.

5. Specialised Use Cases
    - Key-value stores: Caching, session storage (Redis)
    - Document stores: Content management, JSON-based apps (MongoDB)
    - Graph DB: Social networks, recommendation engines (Neo4j)
    - Column stores: Analytics on huge datasets (Cassandra, HBase)

# SQL Constraints (Keys)
## Primary Key

- Purpose: Uniquely identifies each row in a table.
- Primary Key Rules
    - Must be unique — no two rows can have the same primary key value.
    - Must be NOT NULL — cannot contain NULL.
    - Only one primary key is allowed per table (but it can cover multiple columns = composite key).
    - The column(s) used as a primary key should be static (values don’t change often).

- Example:
    ```SQL
    CREATE TABLE Users (
        id INT PRIMARY KEY,
        name VARCHAR(50)
    );

## Foreign Key

- Purpose: Creates a link between two tables.
- Foreign Key Rules: 
    - The referenced table and column must exist before creating the foreign key.
    - The referenced column must be PRIMARY KEY or UNIQUE in the parent table.
    - The data type of both columns (foreign and referenced) must match.
    - You cannot insert a foreign key value that doesn’t exist in the parent table.
    - If you delete a record in the parent table, you must handle it properly using:
        - ON DELETE CASCADE (auto delete child rows)
        - ON DELETE SET NULL
        - ON DELETE RESTRICT

- Example: 
    ```SQL
        CREATE TABLE departments (
            department_id INTEGER PRIMARY KEY,
            department_name VARCHAR(50)
        );

        CREATE TABLE employees (
            employee_id INTEGER PRIMARY KEY,
            last_name VARCHAR(50),
            first_name VARCHAR(50),
            department_id INTEGER,
            FOREIGN KEY (department_id)
                REFERENCES departments(department_id)
                ON DELETE SET NULL -- This is the clause!
        );

## Unique

- Purpose: Ensures all values in a column are unique.
- Unique Constraint Rules:
    - Ensures all values in a column are unique.
    - Allows NULL values (but typically only one NULL).
    - You can define multiple unique columns per table.

- Example: 
    ```SQL
        CREATE TABLE Users (
            id INT PRIMARY KEY,
            email VARCHAR(100) UNIQUE
        );

## Not Null

- Purpose: Ensures a column cannot have NULL values.
- Not Null Constraint Rules:
    - Ensures a column cannot be NULL.
    - Must provide a value during INSERT.
    - Often combined with other constraints (e.g., NOT NULL UNIQUE).

- Example:
    ```SQL
        CREATE TABLE Users (
            id INT PRIMARY KEY,
            name VARCHAR(50) NOT NULL
        );

    > Note: Every user must have a name.

## Default

- Purpose: Provides a default value if none is specified.
- Default Constraint Rules:
    - Used when no value is provided during insert.
    - Must match the column’s data type.
    - Can be used with other constraints.

- Example: 
    ```SQL
        CREATE TABLE Users (
            id INT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            status VARCHAR(20) DEFAULT 'active'
        );

# What is an Index?

- An index is like a book’s index — it helps the database find data faster without scanning the whole table.

## Types of Indexes
| Type                    | Description                                                     | Data Storage                            | Number per Table                                      |
| ----------------------- | --------------------------------------------------------------- | --------------------------------------- | ----------------------------------------------------- |
| **Clustered Index**     | Physically **sorts** the table data by the indexed column       | Table data is stored in **index order** | **1 only** (because table data can be sorted one way) |
| **Non-Clustered Index** | Creates a **separate structure** that points to the actual data | Stores **pointers** to data             | **Many allowed**                                      |


- Example:
    ```SQL
        -- Clustered index (usually on primary key)
        CREATE CLUSTERED INDEX idx_student_id ON Students(student_id);

        -- Non-clustered index (used on columns often searched)
        CREATE NONCLUSTERED INDEX idx_student_name ON Students(name);

### When to Use

1. Clustered Index
    - On Primary Key
    - On columns used in range queries (BETWEEN, ORDER BY, GROUP BY)
    - Example: order_date, id

2. Non-Clustered Index
    - On columns used frequently in WHERE clauses
    - On foreign keys
    - Example: email, status, category

-------

# What is a JOIN?

- A JOIN combines rows from two or more tables based on a related column (usually a foreign key).

## Rule for Joins:

- Both tables must have at least one common column (except CROSS JOIN).
- You must specify how they are related → using ON condition.

- Assume two tables:
    ```SQL
    Students
    +----+----------+
    | id | name     |
    +----+----------+
    | 1  | Alice    |
    | 2  | Bob      |
    | 3  | Carol    |
    | 4  | David    |
    +----+----------+

    Marks
    +----+--------+
    | id | score  |
    +----+--------+
    | 1  | 85     |
    | 2  | 90     |
    | 5  | 70     |
    +----+--------+

### INNER JOIN

- Returns only matching rows from both tables.

    ```SQL
    SELECT s.id, s.name, m.score
    FROM Students s
    INNER JOIN Marks m
    ON s.id = m.id;

- OUTPUT:
    | id | name  | score |
    | -- | ----- | ----- |
    | 1  | Alice | 85    |
    | 2  | Bob   | 90    |


### LEFT JOIN (or LEFT OUTER JOIN)

- **Use:** When you want all records from left table even if no match.
- Returns all rows from left table + matching rows from right.
-  Non-matching rows → right side = NULL.

    ```SQL
    SELECT s.id, s.name, m.score
    FROM Students s
    LEFT JOIN Marks m
    ON s.id = m.id;

- OUTPUT:
    | id | name  | score |
    | -- | ----- | ----- |
    | 1  | Alice | 85    |
    | 2  | Bob   | 90    |
    | 3  | Carol | NULL  |
    | 4  | David | NULL  |

### RIGHT JOIN (or RIGHT OUTER JOIN)
- **Use:** When you want all records from right table.
- Returns all rows from right table + matching rows from left.
- Non-matching left rows → left side = NULL.

    ```SQL
        SELECT s.id, s.name, m.score
        FROM Students s
        RIGHT JOIN Marks m
        ON s.id = m.id;
    
- OUTPUT:
    | id | name  | score |
    | -- | ----- | ----- |
    | 1  | Alice | 85    |
    | 2  | Bob   | 90    |
    | 5  | NULL  | 70    |

### FULL OUTER JOIN

- **Use:** When you need all data, matched or not.
- Returns all rows from both tables.
- Non-matching rows = NULL on missing side.

    ```SQL
    SELECT s.id, s.name, m.score
    FROM Students s
    FULL OUTER JOIN Marks m
    ON s.id = m.id;

- OUTPUT:
    | id | name  | score |
    | -- | ----- | ----- |
    | 1  | Alice | 85    |
    | 2  | Bob   | 90    |
    | 3  | Carol | NULL  |
    | 4  | David | NULL  |
    | 5  | NULL  | 70    |

>Note: Not all DBs support FULL OUTER JOIN (e.g. MySQL before v8).

### CROSS JOIN
- **Use:** Rare; used for generating combinations.
- Returns Cartesian Product (all combinations).
- No ON condition used.

    ```SQL
        SELECT s.name, m.score
        FROM Students s
        CROSS JOIN Marks m;

- OUTPUT:
    | name  | score |
    | ----- | ----- |
    | Alice | 85    |
    | Alice | 90    |
    | Bob   | 85    |
    | Bob   | 90    |
    | Carol | 85    |
    | Carol | 90    |

>Note: Every row of Students is paired with every row of Marks.
Total rows = 3 × 2 = 6.
📌 No ON condition is used.
📌 Mostly used for combinations, testing, or matrix-like data generation.


# Aggregate functions – COUNT, SUM, AVG, MIN, MAX.

| Function    | Description                                                | Example                              | Result         |
| ----------- | ---------------------------------------------------------- | ------------------------------------ | -------------- |
| **COUNT()** | Counts number of rows (or non-NULL values if column given) | `SELECT COUNT(*) FROM employees;`    | Total rows     |
| **SUM()**   | Adds up all numeric values                                 | `SELECT SUM(salary) FROM employees;` | Total salary   |
| **AVG()**   | Calculates average of numeric column                       | `SELECT AVG(salary) FROM employees;` | Average salary |
| **MIN()**   | Finds minimum value                                        | `SELECT MIN(salary) FROM employees;` | Lowest salary  |
| **MAX()**   | Finds maximum value                                        | `SELECT MAX(salary) FROM employees;` | Highest salary |

--------------

# GROUP BY

## Purpose:

- Used to group rows that have the same values in specified columns.
- Usually used with aggregate functions (like COUNT, SUM, AVG, MIN, MAX) to get summary data.

### How it works:

- Groups rows by one or more columns
- Each group returns one row in the result

- Example:
    ```SQL
        SELECT department, COUNT(*) AS total_employees
        FROM employees
        GROUP BY department;

--------

# HAVING

## Purpose:

- Used to filter groups after GROUP BY is applied.
- Key Point:
    - Like WHERE, but for groups, not individual rows
    - Can use aggregate functions in it

- Example:
    ```SQL
        SELECT department, COUNT(*) AS total_employees
        FROM employees
        GROUP BY department
        HAVING COUNT(*) > 5;

----------------

