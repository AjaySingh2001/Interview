# What is Pandas?

- Open-source library.
- Provides data structures like:
- Series → 1D labelled data (like a column in Excel).
- DataFrame → 2D labelled data (like an Excel sheet or SQL table).
- Built on top of NumPy, optimised for performance.

# Why is Pandas used?

- Data handling → Easy to load, clean, and transform datasets (CSV, Excel, SQL, JSON, etc.).
- Analysis → Provides fast operations for filtering, grouping, aggregating, merging, reshaping.
- Exploration → Helps in exploring large datasets with simple methods (head(), describe(), info()).
- Time series → Great support for time-based data.
- Integration → Works well with NumPy, Matplotlib, Scikit-learn.

- Example
    ```python
        import pandas as pd
        # Create DataFrame
        data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
        df = pd.DataFrame(data)

        print(df)
    
> In short: Pandas is like Excel + SQL inside Python, used to make data analysis fast, flexible, and easy.

## Series vs Dataframe

| Feature        | **Series**                    | **DataFrame**                                        |
| -------------- | ----------------------------- | ---------------------------------------------------- |
| **Definition** | 1D labelled array             | 2D labelled data structure (table)                   |
| **Structure**  | Like a single column          | Like an Excel sheet (rows × columns)                 |
| **Data Type**  | Holds data of one type only   | Can hold multiple data types (int, str, float, etc.) |
| **Syntax**     | `pd.Series()`                 | `pd.DataFrame()`                                     |
| **Index**      | Single index                  | Row index + column labels                            |
| **Example**    | `s = pd.Series([10, 20, 30])` | `df = pd.DataFrame({'A': [10, 20], 'B': [30, 40]})`  |
| **Shape**      | (n,)                          | (rows, columns)                                      |
| **Conversion** | DataFrame column = Series     | Collection of Series = DataFrame                     |


# Data Input / Output (I/O)

## READ EXCEL

- Example:
    ```python
        import pandas as pd
        file = pd.read_excel('/content/dummy_employees.xlsx')
        print(file)

        OUTPUT:
            ID        Name  Age Department  Salary Joining_Date
            0      1    Person_1   56  Marketing  115067   2020-01-05
            1      2    Person_2   46      Sales   97215   2020-01-12
            2      3    Person_3   32         IT   99042   2020-01-19
            3      4    Person_4   25    Finance   43284   2020-01-26
            4      5    Person_5   38         HR  102789   2020-02-02
            ..   ...         ...  ...        ...     ...          ...
            195  196  Person_196   23         HR   72344   2023-10-01
            196  197  Person_197   49  Marketing   72918   2023-10-08
            197  198  Person_198   21  Marketing   82224   2023-10-15
            198  199  Person_199   28  Marketing   69298   2023-10-22
            199  200  Person_200   34    Finance  110219   2023-10-29

            [200 rows x 6 columns]

### Read specific sheet

1. Based on indexing
    ```python
        df = pd.read_excel("dummy_employees.xlsx", sheet_name=0)

2. Read multiple sheets at once:

    ```python
    dfs = pd.read_excel("dummy_employees.xlsx", sheet_name=["Sheet1", "Sheet2"])


3. See all Sheet names

    ```python
    excel_file = pd.ExcelFile("dummy_employees.xlsx")
    print(excel_file.sheet_names)

### Columns

1. View Columns

    ```python
        file = pd.read_excel('/content/dummy_employees.xlsx')
        print(file.columns)

        OUTPUT: Index(['ID', 'Name', 'Age', 'Department', 'Salary', 'Joining_Date'], dtype='object')

2. Access Columns

    1. Single Column
        ```python
            file = pd.read_excel('/content/dummy_employees.xlsx')
            print(file['ID'])

            OUTPUT:
            1        2
            2        3
            3        4
            4        5
                ... 
            195    196
            196    197
            197    198
            198    199
            199    200

    2. Multiple Column
        ```python
            file = pd.read_excel('/content/dummy_employees.xlsx')
            print(file[['ID', "Age"]])

            OUTPUT:
            Name: ID, Length: 200, dtype: int64
                  ID  Age
            0      1   56
            1      2   46
            2      3   32
            3      4   25
            4      5   38
            ..   ...  ...
            195  196   23
            196  197   49
            197  198   21
            198  199   28
            199  200   34

    > Note: For multiple columns list of columns inside list is must [['col1', 'col2']]

3. Add New Columns

    ```python
        file = pd.read_excel('/content/dummy_employees.xlsx')
        file['new Col'] =  "New" + file["Name"] #(optional)
        print(file['new Col'])

        OUTPUT:
        0        Person_1New
        1        Person_2New
        2        Person_3New
        3        Person_4New
        4        Person_5New
                ...      
        195    Person_196New
        196    Person_197New
        197    Person_198New
        198    Person_199New
        199    Person_200New
        # Name: new Col, Length: 200, dtype: object

4. Rename existing columns

    ```python
        file = pd.read_excel('/content/dummy_employees.xlsx')
        file.rename(columns={"Name": "Re Name", "Age": "Re Age"}, inplace=True)

>Note: inplace = Apply changes on current data-frame, otherwise it will return new one

5. Delete / Drop

    | Concept         | Meaning                   |
    | --------------- | ------------------------- |
    | `drop()`        | Removes rows/columns      |
    | `axis=0`        | Drop by row labels        |
    | `axis=1`        | Drop by column names      |
    | `inplace=True`  | Change original DataFrame |
    | `inplace=False` | Return new DataFrame      |


- Drop Columns:

    ```python
        file = pd.read_excel('/content/dummy_employees.xlsx')
        df.drop("Bonus", axis=1, inplace=True)           # Drop one column
        df.drop(["Age", "Salary"], axis=1, inplace=True) # Drop multiple

- Drop Rows:

    ```python
        file = pd.read_excel('/content/dummy_employees.xlsx')
        df.drop(2, axis=0, inplace=True)


>Note: We can use **error: ignore** to ignore the errors: df.drop("Bonus", axis=1, inplace=True, **errors='ignore'**)

6. Reorder Columns

    ```python
        file = pd.read_excel('/content/dummy_employees.xlsx')
        new_file = file[["column1", "column3", "column2", "column4"]] # Just accessing the columns according to our need

>Note: This will not affect the original file but return the new one.

7. Change Data Type

    ```python
        df["Age"] = df["Age"].astype(float)

8. Rename All Columns (at once)

    ```python
        df.columns = ["ID", "Name", "Age", "Dept", "Salary", "JoinDate"]

| Concept                 | Explanation                                   |
| ----------------------- | --------------------------------------------- |
| **In-place**            | ✅ Works directly (no need for `inplace=True`) |
| **Length check**        | Must match number of existing columns         |
| **Affects all columns** | You can’t rename just one this way            |
| **No data change**      | Only header names change                      |


9. Check for Missing Values

    ```python
        df["Salary"].isnull().sum()

        OUTPUT:
            ID   Name  Re Age  Department  Salary  new Col
        0    False  False   False       False   False    False
        1    False  False   False       False   False    False
        3    False  False   False       False   False    False
        4    False  False   False       False   False    False
        5    False  False   False       False   False    False
        ..     ...    ...     ...         ...     ...      ...
        195  False  False   False       False   False    False
        196  False  False   False       False   False    False
        197  False  False   False       False   False    False
        198  False  False   False       False   False    False
        199  False  False   False       False   False    False


10. Fill Values

    ```python
        file.fillna("NEW", inplace=True)     #all null
        file["Column"].fillna("NEW", inplace=True)     #specified column

>Note: multiple columns are not allowed

11. Replace Values

    ```python
        file["Department"]=file["Department"].replace("HR", "Human Resource")
    
>Note: inplace=True will consider dataframe as copy after python 3.0

12. Apply Functions to Columns

    ```python
        df["Name"] = df["Name"].apply(str.upper)

>Note: inplace=True will not work here because apply return a new data frame


13. Select Columns by Data Type

    ```python
        df.select_dtypes(include="number").head()

14. Create Columns Using Conditions

    ```python
        df["Status"] = df["Salary"].apply(lambda x: "High" if x > 80000 else "Low")

15. Drop duplicates

    - drop_duplicates() is used to remove duplicate rows from a DataFrame.
        ```python
            import pandas as pd

            df = pd.DataFrame({
                'Name': ['John', 'Mary', 'John', 'Alex', 'Mary'],
                'Department': ['IT', 'HR', 'IT', 'IT', 'HR'],
                'Salary': [50000, 60000, 50000, 55000, 60000]
            })

            df.drop_duplicates()

            df.drop_duplicates(keep='last') # first/last/False


            # Remove duplicates based on 'Name' only
            df.drop_duplicates(subset=['Name'])

            df.drop_duplicates(subset=['Name'], inplace=True)

    | Parameter | Purpose                                 |
    | --------- | --------------------------------------- |
    | `subset`  | Specify columns to consider             |
    | `keep`    | 'first', 'last', or False               |
    | `inplace` | Modify original DataFrame or return new |


------------

# Common Parameters

## index_col

- Specifies which column(s) should be used as the row index of the DataFrame.

    ```python
        df = pd.read_excel("dummy_employees.xlsx", index_col=0)

        df = pd.read_excel("dummy_employees.xlsx", index_col=["Department", "Name"])

> Note: This makes the first column (index 0) the DataFrame index instead of the default 0,1,2,...(default range)
> Can not use index-col with single column otherwise get  **Empty DataFrame**

## usecols

- Loads only specific columns from the file (by name or index).

    ```python
        df = pd.read_excel("dummy_employees.xlsx", usecols=["Department"])
        df = pd.read_excel("dummy_employees.xlsx", usecols=["Name", "Salary"])

        OUTPUT:
            Department
        0    Marketing
        1        Sales
        2           IT
        3      Finance
        4           HR
        ..         ...
        195         HR
        196  Marketing
        197  Marketing
        198  Marketing
        199    Finance

## skiprows

- Skips a given number (or list) of rows from the top of the file.

    ```python
    df = pd.read_excel("dummy_employees.xlsx", skiprows=2) #skip rows from 0
    file3 = pd.read_excel('/content/dummy_employees.xlsx', index_col=0, usecols=["ID","Department","Salary"], skiprows=[4, 7, 9] ) # skip specific rows

>Note: we can use it with the use-col because it will tries to skip the column ro as well unless or until we are not skipping the particular row 

## astype

- In Pandas, astype() is used to convert the data type of a Series or DataFrame column to another type.

- **Series.astype(dtype, copy=True, errors='raise')**
    - dtype: target data type (e.g., int, float, str, 'category', 'datetime64').
    - copy: if True, always returns a new object; if False.
    - errors:
        - 'raise' → raise error if conversion fails (default)
        - 'ignore' → return original if conversion fails
    
>Note: Does not apply inplace changes

# DataFrame Basics

## Viewing data (head(), tail(), shape, info(), describe())

1. df.head(n)

    - Shows the first n rows of the DataFrame.
    - Default n=5.

    ```python
    file = pd.read_excel('/content/dummy_employees.xlsx', index_col=0, usecols=["ID","Department","Salary"], skiprows=[4, 7, 9] )

    print(file.head(count))

2. df.tail(n)

    - Shows the last n rows of the DataFrame.
    - Default n=5.
    
    ```python
        file = pd.read_excel('/content/dummy_employees.xlsx', index_col=0, usecols=["ID","Department","Salary"], skiprows=[4, 7, 9] )
        
        print(file.tail(count))

3. df.shape

    - Returns a tuple (rows, columns) showing DataFrame dimensions.

    ```python
        df.shape

        OUTPUT:
        (100, 5)

        100 → number of rows
        5 → number of columns
    
4. df.info()

- Gives a summary of the DataFrame:
    - Column names
    - Data types
    - Non-null counts
    - Memory usage

    ```python
        df.info()

        OUTPUT:
        <class 'pandas.core.frame.DataFrame'>
            RangeIndex: 200 entries, 0 to 199
            Data columns (total 6 columns):
            #   Column        Non-Null Count  Dtype         
            ---  ------        --------------  -----         
            0   ID            200 non-null    int64         
            1   Name          200 non-null    object        
            2   Age           200 non-null    int64         
            3   Department    200 non-null    object        
            4   Salary        200 non-null    int64         
            5   Joining_Date  200 non-null    datetime64[ns]
            dtypes: datetime64[ns](1), int64(3), object(2)
            memory usage: 9.5+ KB

>Note: No need to call inside print, it will directly shows all the informations.

5. df.describe()

- Generates summary statistics for numeric columns (mean, std, min, max, quartiles).

    ```python
        df.describe() # default numeric
        df.describe(include="object") #for string values columns
        df.describe(include="all") # for all the columns


**OUTPUT:**
|index|ID|Age|Salary|Joining\_Date|
|---|---|---|---|---|
|count|200\.0|200\.0|200\.0|200|
|mean|100\.5|38\.665|76591\.945|2021-12-01 12:00:00|
|min|1\.0|18\.0|30412\.0|2020-01-05 00:00:00|
|25%|50\.75|27\.75|54278\.0|2020-12-18 06:00:00|
|50%|100\.5|40\.0|74453\.5|2021-12-01 12:00:00|
|75%|150\.25|49\.25|98598\.0|2022-11-14 18:00:00|
|max|200\.0|59\.0|119930\.0|2023-10-29 00:00:00|
|std|57\.879184513951124|12\.604648380816508|26566\.93411883176|NaN|

--------

# Column access: df['col'], df[['col1','col2']]

- Single and multiple
    ```python
        file[['Department', 'Age']] # multiple columns
        file['Department'] # single column

        OUTPUT:
                Department	Age
            0	Marketing	56
            1	Sales	46
            2	IT	32
            3	Finance	25
            4	HR	38

-------------

# Row access: loc[], iloc[]

1. iloc[] → Index-based Access

    - Uses integer positions (0-based).
    - Syntax: df.iloc[row_index, column_index]

    ```python
        file.iloc[10:20] # for all column
        file.iloc[range, column_index] # for specific column

    OUTPUT:

            Department
        10	Sales
        11	Sales
        12	Finance
        13	Sales
        14	Finance
        15	IT
        16	Finance
        17	Finance
        18	Sales
        19	Sales

2. loc[] → Label-based Access

    - Uses row and column labels.
    - Syntax: df.loc[row_label, column_label]

    ```python
        # If index is default 0,1,2...
        df.loc[0]             # first row
        df.loc[0:5]           # rows 0 to 5 inclusive

        # Access specific cell
        df.loc[2, 'Salary']

        # Access multiple columns for a row
        df.loc[2, ['Name', 'Salary']]

    
3. loc[] → Label-based Access

    - Uses row and column labels.
    - Syntax: df.loc[row_label, column_label]

    ```python
        # If index is default 0,1,2...
        df.loc[0]             # first row
        df.loc[0:5]           # rows 0 to 5 inclusive

        # Access specific cell
        df.loc[2, 'Salary']

        # Access multiple columns for a row
        df.loc[2, ['Name', 'Salary']]

-------------



# Aggregation & Grouping

1. Grouping Data: groupby()

    - groupby() splits your DataFrame into groups based on column values.
    - Then you can apply aggregation functions like sum(), mean(), count(), etc.

        ```python
            import pandas as pd

            df = pd.DataFrame({
                'Department': ['IT', 'HR', 'IT', 'HR', 'IT'],
                'Salary': [50000, 60000, 55000, 65000, 52000],
                'Age': [25, 30, 28, 35, 26]
            })

            # Group by Department
            grouped = df.groupby('Department') #multiple columns 


>Note: It returns a **DataFrameGroupBy object** — a special grouped object that you can use to perform aggregation, iteration, or transformation.

2. Aggregation Functions
    
    ```python

        grouped = file.groupby(['Department', 'Age'])['Salary'].sum()


| Function/Method    | Purpose                               |
| ------------------ | ------------------------------------- |
| `groupby()`        | Split DataFrame into groups           |
| `sum()`            | Sum of numeric values per group       |
| `mean()`           | Mean of numeric values per group      |
| `count()`/`size()` | Count rows per group                  |
| `agg()`            | Apply multiple or custom aggregations |

-----------------------

# Series methods
## Basic Arithmetic Operations
| Operation        | Method                                                      |
| ---------------- | ----------------------------------------------------------- |
| Addition         | `Series.add(other, fill_value=None)`                        |
| Subtraction      | `Series.sub(other, fill_value=None)` or `Series.subtract()` |
| Multiplication   | `Series.mul(other, fill_value=None)` or `Series.multiply()` |
| Division         | `Series.div(other, fill_value=None)` or `Series.divide()`   |
| Floor Division   | `Series.floordiv(other, fill_value=None)`                   |
| Modulus          | `Series.mod(other, fill_value=None)`                        |
| Power / Exponent | `Series.pow(other, fill_value=None)`                        |

## Unary Arithmetic Operations

| Operation | Method                     |
| --------- | -------------------------- |
| Absolute  | `Series.abs()`             |
| Negation  | `Series.neg()`             |
| Rounding  | `Series.round(decimals=0)` |

## Cumulative / Aggregate Arithmetic Operations

| Operation          | Method             |
| ------------------ | ------------------ |
| Cumulative sum     | `Series.cumsum()`  |
| Cumulative product | `Series.cumprod()` |
| Cumulative min     | `Series.cummin()`  |
| Cumulative max     | `Series.cummax()`  |

## Other Useful Arithmetic Methods

| Operation            | Method                                             |
| -------------------- | -------------------------------------------------- |
| Clip values          | `Series.clip(lower=None, upper=None)`              |
| Multiply with factor | `Series.mul(other, fill_value=None)` (same as `*`) |
| Add with factor      | `Series.add(other, fill_value=None)` (same as `+`) |

## Series comparisons

| Method             | Equivalent Operator | Example     |
| ------------------ | ------------------- | ----------- |
| `Series.eq(other)` | `==`                | `s1.eq(s2)` |
| `Series.ne(other)` | `!=`                | `s1.ne(s2)` |
| `Series.gt(other)` | `>`                 | `s1.gt(s2)` |
| `Series.ge(other)` | `>=`                | `s1.ge(s2)` |
| `Series.lt(other)` | `<`                 | `s1.lt(s2)` |
| `Series.le(other)` | `<=`                | `s1.le(s2)` |


#  Common buil in aggregated functions

| Function    | Description               |
| ----------- | ------------------------- |
| `sum()`     | Sum of values             |
| `mean()`    | Mean (average)            |
| `median()`  | Median value              |
| `mode()`    | Most frequent value       |
| `min()`     | Minimum value             |
| `max()`     | Maximum value             |
| `count()`   | Number of non-null values |
| `nunique()` | Number of unique values   |
| `std()`     | Standard deviation        |
| `var()`     | Variance                  |
| `prod()`    | Product of values         |
| `first()`   | First value in group      |
| `last()`    | Last value in group       |

------------

# query() Method
- Filter rows in a DataFrame using a SQL-like expression for better readability and performance.
- Syntax
    - DataFrame.query(expr, inplace=False, **kwargs)

    ```python
        import pandas as pd

        df = pd.DataFrame({
            "product_id": [0, 1, 2, 3, 4],
            "low_fats": ["Y", "Y", "N", "Y", "N"],
            "recyclable": ["N", "Y", "Y", "Y", "N"]
        })

        result = df.query('low_fats == "Y" and recyclable == "Y"')
        print(result)


# Questions

1. Creating a Series
    ```python
        import pandas as pd

        sr = [1,2,4,5,6]
        print(pd.Series(sr))

        OUTPUT:
        0    1
        1    2
        2    4
        3    5
        4    6

2. Series to List Conversion
    ```python
        sr = [1,2,4,5,6]

        series = pd.Series(sr)
        print(type(series))

        srtolst = series.to_list()
        print(type(srtolst))
        print(srtolst)

        OUTPUT:
        <class 'pandas.core.series.Series'>
        <class 'list'>
        [1, 2, 4, 5, 6]

3. Write a Pandas program to add, subtract, multiple and divide two Pandas Series.

    ```python
        # SEries arithmatic
        a,b = [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]
        print(a)
        print(b)

        sa = pd.Series(a)
        sb = pd.Series(b)
        print(sa)
        print(sb)
        print(sa.add(sb)) # Add

        print("sub", sa.sub(sb)) # Subtract

        print("Mul", sa.mul(sb)) # multiply

        print("Div", sa.div(sb)) # divide

4. Compare the elements of the two Pandas Series.

    ```python
        a,b = [2, 4, 6, 8, 10], [1, 3, 5, 7, 10]
        sa = pd.Series(a)
        sb = pd.Series(b)
        print("Equal", sa.eq(sb)) # Equal
        print("Greater then equal to", sa.ge(sb)) # ge
        print("Greater Then", sa.gt(sb)) # gt
        print("Less Then", sa.lt(sb)) # lt
    
        OUTPUT:
        Equal 0    False
            1    False
            2    False
            3    False
            4     True

>Note: pd.Series() automatically takes the keys as the index and values as the data.

5. Numpy array to series

    ```python

        a = np.array([10, 20, 30, 40, 50])
        s = pd.Series(a)

        print(type(a))

        print(pd.Series(a))


6. Change Series DataType

    ```python
        b = [2, 4, 6, 8, 10]

        s = pd.Series(b)

        print(s.dtype)

        s2 = s.astype(bool, copy=False)

        print(s2)

7. Convert the first column of a DataFrame as a Series.

    ```python
        data = {
            'Name': ['Alice', 'Bob', 'Charlie'],
            'Age': [25, 30, 35],
            'City': ['New York', 'London', 'Paris']
        }


        df = pd.DataFrame(data)
        print(pd.Series(data['Name']))

8. Series to Array

    ```python
        # Series to array
        s = ['100', '200', 'python', '300.12', '400']
        s1 = pd.Series(s)
        print(s1.dtype)

        s2 = s1.to_numpy()
        print(type(s2))
        print(s2)

        OUTPUT:
            object
            <class 'numpy.ndarray'>
            ['100' '200' 'python' '300.12' '400']

9. Flatten Series of Lists

    ```python
        # Example Series: each element is a list
        s = pd.Series([[1, 2, 3], [4, 5], [6]])

        # Step 1: Expand each list in the Series into separate columns of a DataFrame
        # apply(pd.Series) takes each element of the Series (a list) and converts it into a row of a DataFrame
        df_expanded = s.apply(pd.Series)
        """
        Example df_expanded:
            0    1    2
        0    1    2  3.0
        1    4    5  NaN
        2    6  NaN  NaN
        """

        # Step 2: Stack the DataFrame to convert columns into a single Series
        # stack() compresses the DataFrame into a single column (Series) and drops NaN values by default
        s_stacked = df_expanded.stack()
        """
        Example s_stacked (MultiIndex):
        0  0    1
        1    2
        2    3
        1  0    4
        1    5
        Example s_flattened:
        0    1
        1    2
        2    3
        3    4
        4    5
        5    6
        dtype: int64
        """

        # Final flattened Series
        print(s_flattened)

        Process:
        1. convert all into series
        2. stack them using stack()
        3. then reset index by using the reset_index(drop=True)


10. sort the series
    ```python
        # 1st way
        s = ['100', '200', 'python', '300.12', '400']
        s1 = pd.Series(s).sort_values()
        print(s1)

        # 2nd way
            convert into list and then sort and again convert it into series
        s2 = s1.to_list()
        for _ in range(len(s2)):
            for i in range(0, len(s2)-1):
                if s2[i]>s2[i+1]:
                    s2[i], s2[i+1] = s2[i+1],s2[i]
        print(pd.Series(s2))



11. Creating a DataFrame from a Dictionary
    ```python
        d = {
            "Name": [11,22,33,44,55],
            "Age": ["dsf", "skldfn", "dsifjn"]
        }
        print(pd.DataFrame(d, ))
    
12. Selecting Specific Columns and Rows

    ```python
        df = pd.DataFrame(exam_data)
        df.loc[1:7, ["name", "qualify"]]


13. Selecting Rows Where Attempts > 2

    ```python
        df[df['attempts']>2]
        
>Note: In Pandas, the syntax df[condition] is called Boolean indexing.

14. Apply multiple conditions

    ```python
        df.loc[(df['score']>15) & (df['attempts']<2)]

15. Rename Column

    ```python
        df.rename(columns={"name": "Student"}, inplace=True)



# Joins and Merging
## Merge
- pd.merge() combines two DataFrames based on one or more common columns (keys) — just like SQL joins.
- It matches rows from both DataFrames using those keys.
- Syntax:
    **pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None)**

    | Parameter              | Description                                                    |
    | ---------------------- | -------------------------------------------------------------- |
    | `left`, `right`        | DataFrames to merge                                            |
    | `how`                  | Type of join: `'inner'`, `'outer'`, `'left'`, `'right'`        |
    | `on`                   | Column(s) common to both DataFrames to join on                 |
    | `left_on` / `right_on` | Use if the column names differ between the DataFrames          |
    | `suffixes`             | Add suffixes to overlapping column names (e.g. `('_x', '_y')`) |


1. Join DataFrames along Rows (Join Rows)
    ```python
        # DataFrame 1
        s1 = pd.DataFrame({
            "student_id": ["S1", "S2", "S3", "S4", "S5"],
            "name": ["Danniella Fenton", "Ryder Storey", "Bryce Jensen", "Ed Bernal", "Kwame Morin"],
            "marks": [200, 210, 190, 222, 199]
        })

        # DataFrame 2
        s2 = pd.DataFrame({
            "student_id": ["S4", "S5", "S6", "S7", "S8"],
            "name": ["Scarlette Fisher", "Carla Williamson", "Dante Morse", "Kaiser William", "Madeeha Preston"],
            "marks": [201, 200, 198, 219, 201]
        })

        pd.concat([s1, s2], axis=0) # default axis = 0(row), optional axis=1(column)


2. Join DataFrames along Columns (Join Columns)
    ```python
        # Student details
        students = pd.DataFrame({
            'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
            'name': ['Ajay', 'Riya', 'Karan', 'Tina', 'Maya'],
            'city': ['Delhi', 'Mumbai', 'Pune', 'Delhi', 'Chennai']
        })

        # Exam scores
        scores = pd.DataFrame({
            'id': ['S3', 'S4', 'S5', 'S6', 'S7'],
            'marks': [85, 90, 78, 88, 92],
            'subject': ['Maths', 'Science', 'English', 'Maths', 'Science']
        })

        # Inner Join: Provide common rows
        pd.merge(students, scores, left_on='student_id', right_on='id', how='inner')


        # Left Join: All records of left side. All from students + matches from scores.
        pd.merge(students, scores, left_on='student_id', right_on='id', how='left')

        # Right Join: Keep all scores, even if the student isn’t in the students table.
        pd.merge(students, scores, left_on='student_id', right_on='id', how='right')


        # Outer Join: Keep all records from both DataFrames.
        pd.merge(students, scores, left_on='student_id', right_on='id', how='outer')


        # Customising Overlapping Column Names: Avoid duplicate column names (student_id and id):
        pd.merge(students, scores, left_on='student_id', right_on='id', how='outer', suffixes=('_student', '_score'))

        In above case if there are columns with the same in each table then we use suffix then so it will not be overriden. and it will look like name_student, and name_score in output


3. Append Rows to Existing DataFrame
    ```python
        students = pd.DataFrame({
            'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
            'name': ['Ajay', 'Riya', 'Karan', 'Tina', 'Maya'],
            'city': ['Delhi', 'Mumbai', 'Pune', 'Delhi', 'Chennai']
        })

        students.loc[len(students)] = ['S6', 'Aarav', 'Kolkata']

        # Add multiple data
        new_row = pd.DataFrame({
            'student_id': ['S7'],
            'name': ['gaurav'],
            'city': ['Kolkata']
        })
        students = pd.concat([students, new_row], ignore_index=True)

>Note: ignore_index=True: Reset index follow the default ones otherwise it will starts from 0 for the concatinated once.

4. Append List of Dictionaries/Series

    ```python
        students = pd.DataFrame({
            'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
            'name': ['Som', 'Riya', 'Karan', 'Tina', 'Maya'],
            'city': ['Delhi', 'Mumbai', 'Pune', 'Delhi', 'Chennai']
        })

        students.loc[len(students)] = ['S6', 'Aarav', 'Kolkata']
        new_row = pd.DataFrame({
            'student_id': ['S7'],
            'name': ['gaurav'],
            'city': ['Kolkata']
        })
        students = pd.concat([students, new_row], ignore_index=True)
        data = [
                ['S5', 'Tina', 'Delhi'],
                ['S6', 'Tin1', 'Delhi'],
                ['S7', 'Tin2', 'Delhi'],
                ['S8', 'Tin3', 'Delhi'],
                ['S9', 'Tin4', 'Delhi']
            ]
        series = pd.DataFrame(data, columns=students.columns)  
        students = pd.concat([students, series], ignore_index=True)

        # add list of dictionaries
        new_data = [
            {'student_id': 'S11', 'name': 'qwe', 'city': 'Delhi'},
            {'student_id': 'S12', 'name': '12we', 'city': 'Chennai'},
            {'student_id': 'S13', 'name': 'qwe11', 'city': 'Kolkata'}
        ]

        students = pd.concat([students, pd.DataFrame(new_data)], ignore_index=True)
        students


5. Join Rows and Merge with Another DataFrame: Write a Pandas program to join the two given dataframes along rows and merge with another dataframe along the common column id.

    ```python
        Write a Pandas program to join the two given dataframes along rows and merge with another dataframe along the common column id.


        # Student DataFrame 1
        student_data1 = pd.DataFrame({
            'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
            'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'],
            'marks': [200, 210, 190, 222, 199]
        })

        # Student DataFrame 2
        student_data2 = pd.DataFrame({
            'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
            'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'],
            'marks': [201, 200, 198, 219, 201]
        })

        concat = pd.concat([student_data1, student_data2], ignore_index=True)

        # Exam DataFrame
        exam_data = pd.DataFrame({
            'student_id': ['S1', 'S2', 'S3', 'S4', 'S5', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13'],
            'exam_id': [23, 45, 12, 67, 21, 55, 33, 14, 56, 83, 88, 12]
        })

        merged_data = pd.merge(concat, exam_data, on="student_id")
        merged_data

    
## Grouping and aggregating

1. Grouping by School Code: Write a Pandas program to split the following dataframe into groups based on school code. Also check the type of GroupBy object.

    ```python
        data = pd.DataFrame({
            'school': ['s001', 's002', 's003', 's001', 's002', 's004'],
            'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
            'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
            'date_Of_Birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
            'age': [12, 12, 13, 13, 14, 12],
            'height': [173, 192, 186, 167, 151, 159],
            'weight': [35, 32, 33, 30, 31, 32],
            'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
        }, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])


        data.count()
        d = data.groupby("school")
        for school, group in d:
            print(school)
            print(group)

2. Grouping by School Code with Age Aggregation: Write a Pandas program to split the following dataframe by school code and get mean, min, and max value of age for each school.

    ```python
        group = data.groupby("school")

        print("Mean age for each school:")
        print(group["age"].mean())

        print("\nMax age for each school:")
        print(group["age"].max())

        print("\nMin age for each school:")
        print(group["age"].min())

3. Grouping by School Code and Class: Write a Pandas program to split the following given dataframe into groups based on school code and class, and call specific group.

    ```python
        data = pd.DataFrame({
            'school': ['s001', 's002', 's003', 's001', 's002', 's004'],
            'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
            'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
            'date_Of_Birth': ['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998', '11/05/2002', '15/09/1997'],
            'age': [12, 12, 13, 13, 14, 12],
            'height': [173, 192, 186, 167, 151, 159],
            'weight': [35, 32, 33, 30, 31, 32],
            'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
        }, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

        d = data.groupby("school")
        # {school:group.to_dict("records") for school, group in d}

        list(d)

        # call specific group
        print(d.get_group("s001"))


4. Grouping by Two Columns and Sorting Aggregated Results: Write a Pandas program to split a dataset to group by two columns and then sort the aggregated results within the groups.

    ```python
        import pandas as pd

        # Create sample dataset with order details
        data = pd.DataFrame({
            'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
            'purch_amt': [150.50, 270.65, 65.26, 110.50, 948.50, 2400.60, 5760.00, 1983.43, 2480.40, 250.45, 75.29, 3045.60],
            'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', 
                        '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', 
                        '2012-08-17', '2012-04-25'],
            'customer_id': [3005, 3001, 3002, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002],
            'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]
        })

        # 1️⃣ Group the data by 'customer_id' and 'salesman_id'
        # Each combination (customer, salesman) will form a separate group
        # Then aggregate the total purchase amount per pair using sum()
        new_data = data.groupby(["customer_id", "salesman_id"]).agg({"purch_amt": sum}) 

        # 2️⃣ Re-group by only 'customer_id' (level=0 in MultiIndex)
        #    'group_keys=False' prevents pandas from adding extra grouping labels
        #    Then, inside each customer group, select the top purchase amounts
        sorted_data = new_data.groupby(level=0, group_keys=False)["purch_amt"].nlargest()

        # 3️⃣ Display the final result showing:
        #    - Each customer_id
        #    - Corresponding salesman_id
        #    - Total purchase amount (sorted descending within each group)
        print(sorted_data)


5.  Grouping by Customer ID with List of Order Dates: Write a Pandas program to split the following dataframe into groups based on customer id and create a list of order date for each group.

    ```python
        data = pd.DataFrame({
            'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
            'purch_amt': [150.50, 270.65, 65.26, 110.50, 948.50, 2400.60, 5760.00, 1983.43, 2480.40, 250.45, 75.29, 3045.60],
            'ord_date': ['2012-10-05', '2012-09-10', '2012-10-05', '2012-08-17', '2012-09-10', 
                        '2012-07-27', '2012-09-10', '2012-10-10', '2012-10-10', '2012-06-27', 
                        '2012-08-17', '2012-04-25'],
            'customer_id': [3005, 3001, 3002, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002],
            'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]
        })

        new_data = data.groupby("customer_id")["ord_date"].apply(list)
        new_data

6. Grouping by Customer ID – Purchase Amount Aggregation: Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group. Using the following dataset find the mean, min, and max values of purchase amount (purch_amt) group by customer id (customer_id).

    ```python
        import pandas as pd

        data = {
            "ord_no": [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
            "purch_amt": [150.50, 270.65, 65.26, 110.50, 948.50, 2400.60, 5760.00, 1983.43, 2480.40, 250.45, 75.29, 3045.60],
            "ord_date": ["2012-10-05", "2012-09-10", "2012-10-05", "2012-08-17", "2012-09-10", 
                        "2012-07-27", "2012-09-10", "2012-10-10", "2012-10-10", "2012-06-27", 
                        "2012-08-17", "2012-04-25"],
            "customer_id": [3005, 3001, 3002, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002],
            "salesman_id": [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]
        }

        df = pd.DataFrame(data)
        result = df.groupby("customer_id")
        result.agg({"purch_amt": ["mean", "min", "max"]})

7. Grouping by Two Columns with Row Count: Write a Pandas program to split a dataset to group by two columns and count by each row.

    ```python
        import pandas as pd

        data = {
            "ord_no": [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
            "purch_amt": [150.50, 270.65, 65.26, 110.50, 948.50, 2400.60, 5760.00, 1983.43, 2480.40, 250.45, 75.29, 3045.60],
            "ord_date": ["2012-10-05", "2012-09-10", "2012-10-05", "2012-08-17", "2012-09-10", 
                        "2012-07-27", "2012-09-10", "2012-10-10", "2012-10-10", "2012-06-27", 
                        "2012-08-17", "2012-04-25"],
            "customer_id": [3005, 3001, 3002, 3009, 3005, 3007, 3002, 3004, 3009, 3008, 3003, 3002],
            "salesman_id": [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]
        }

        df = pd.DataFrame(data)

        result = df.groupby(["customer_id", "salesman_id"]).size().reset_index(name="row_count")
        result

>**Note:** Converts an series into the dataframe with the index column name as row_count

# Leetcode Questions

1. A country is big if:
    - it has an area of at least three million (i.e., 3000000 km2), or
    - it has a population of at least twenty-five million (i.e., 25000000).

    ```python
        data = {
            "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
            "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
            "area": [652230, 28748, 2381741, 468, 1246700],
            "population": [25500100, 2831741, 37100000, 78115, 20609294],
            "gdp": [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]
        }

        world = pd.DataFrame(data)

        #Basic version

            # new_data = world[(world["population"]>=25000000) | (world["area"]>=3000000)]
            # new_data[["name", "population", "area"]]

        #Optimized Version
        new_data = world.loc[(world["population"]>=25000000) | (world["area"]
        >=3000000), ["name", "population", "area"]]

        #more refind
        new_data = world.query('population >= 25000000 or area >= 3000000')[["name", "population", "area"]]

        new_data


2. Write a solution to find the ids of products that are both low fat and recyclable.
    - Return the result table in any order. The result format is in the following example.

    ```python
        data = {
            "product_id": [0, 1, 2, 3, 4],
            "low_fats": ["Y", "Y", "N", "Y", "N"],
            "recyclable": ["N", "Y", "Y", "Y", "N"]
        }
        df = pd.DataFrame(data)
        # df.loc[((df["low_fats"]=="Y") & (df['recyclable']=="Y")), ["product_id"]]
        df.query('low_fats == "Y" and recyclable == "Y"')[["product_id"]]

    
3. Write a solution to find all customers who never order anything.
= Return the result table in any order. The result format is in the following example.

    ```python
        # Customers table
        customers_data = {
            "id": [1, 2, 3, 4],
            "name": ["Joe", "Henry", "Sam", "Max"]
        }
        customers = pd.DataFrame(customers_data)

        # Orders table
        orders_data = {
            "id": [1, 2],
            "customerId": [3, 1]
        }
        orders = pd.DataFrame(orders_data)

        customers.loc[~customers['id'].isin(orders['customerId']), ["name"]].rename(columns={"name":"Customers"})
    ```

4. Write a solution to find all the authors that viewed at least one of their own articles.Return the result table sorted by id in ascending order. The result format is in the following example.

    ```python
        data = {
            "article_id": [1, 1, 2, 2, 4, 3, 3],
            "author_id": [3, 3, 7, 7, 7, 4, 4],
            "viewer_id": [5, 6, 7, 6, 1, 4, 4],
            "view_date": [
                "2019-08-01",
                "2019-08-02",
                "2019-08-01",
                "2019-08-02",
                "2019-07-22",
                "2019-07-21",
                "2019-07-21",
            ],
        }


        df = pd.DataFrame(data)
        pd.DataFrame({"id": sorted(pd.Series(df.query("author_id == viewer_id")["author_id"].unique()))})


5. Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase. Return the result table ordered by user_id.

    ```python
        data = {
            "user_id": [1, 2],
            "name": ["aLice", "bOB"]
        }

        users = pd.DataFrame(data)

        users["name"] = users["name"].str.capitalize()
        users[['user_id']].sort_values(by="user_id", ascending=True)


6. Write a solution to find the users who have valid emails. 
    - A valid e-mail has a prefix name and a domain where:
    - The prefix name is a string that may contain letters (upper or lower case), digits underscore '_', period '.', and/or dash '-'. 
    - The prefix name must start with a letter.
    - The domain is '@leetcode.com'.

        ```python
            data = {
                "user_id": [1, 2, 3, 4, 5, 6, 7],
                "name": ["Winston", "Jonathan", "Annabelle", "Sally", "Marwan", "David", "Shapiro"],
                "mail": [
                    "winston@leetcode.com",
                    "jonathanisgreat",
                    "bella-@leetcode.com",
                    "sally.come@leetcode.com",
                    "quarz#2020@leetcode.com",
                    "david69@gmail.com",
                    ".shapo@leetcode.com"
                ]
            }

            users = pd.DataFrame(data)

            users.loc[users['mail'].str.match(r'^[A-Za-z0-9][A-Za-z0-9._-]*@leetcode\.com$')]

