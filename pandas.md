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
