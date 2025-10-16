# Decorator

## What is decorator and why we use it?

- A function which takes another function as an input and add extra functionality to it.

### Why we use inner function(nested function)?

- Inner function replicate the input function. The outer function sets up the decorator once, and the inner function runs each time the decorated function is called.

- **Without outer function:** Without an inner function, a decorator cannot add behaviour around the original function and just returns it as-is.

    ``` python
    Example 1: 
    
        from functools import wraps // Preserve function metadata

        def wrapper(f):
            @wraps(f)
            def inner(*a, **ka):
                result = f()
                print("result: ", result)
                return result*10
            return  inner


        @wrapper
        def sum(a=10, b=20):
            """Add 2 numbers"""
            return a+b
            
            
        sum()
        print(sum.__name__) without @wraps: inner/ with wrap: sum
        print(sum.__doc__) without @wraps: None/ with wrap: Add 2 numbers

    Example 2: 

        def login_required(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            return func(request, *args, **kwargs)
        return wrapper
    ```

# Generator/Iterator

## Iterator:

- An iterator is an object that you can loop over with next() — it remembers where it left off.
- Does not work with sets, dictionary
- It implements two methods:
    * __iter__()
    * __next__()

    ``` python
        nums = [1, 2, 3]
        it = iter(nums)
        print(next(it))  # 1
        print(next(it))  # 2
        print(next(it))  # 3

    ```

## Generator:

- A generator is a shortcut to create an iterator using the yield keyword.
- It produces values one at a time, pausing after each yield.

    ``` python
        def counter():
            for i in range(1, 4):
                yield i

        gen = counter()
        print(next(gen))  # 1
        print(next(gen))  # 2
    ```

### Difference between these functions:

``` python
fun 1: 
    def counter():
        for i in range(1,10):
            yield i

    gen = counter()
    print(next(gen))
    print(next(gen))
    print(next(gen))

fun 2:
    def counter():
        for i in range(1,10):
            yield i
            
    print(next(counter()))
    print(next(counter()))
    print(next(counter()))
```

### Does this work?
```python
    Below expression will create generator object:<generator object <genexpr> at 0x7a0949456380>
    
    nums = (x * 2 for x in range(5))

    print(next(nums))  # 0
    print(next(nums))  # 2

```

### Difference between:
```python

    lst = [x for x in range(1000000)]
    gen = (x for x in range(1000000))
```

# Python Method Types:

## 1. Normal Instance Method  (Works on object-specific data)

- First argument: self → refers to the object instance
- Scope: Can access instance variables and class variables
- Use case: When method needs to work with object-specific data

    ```python
    class Student:
        school = "ABC School"

        def __init__(self, name):
            self.name = name  # instance variable

        def greet(self):
            return f"Hello {self.name} from {self.school}"

    s1 = Student("Ajay")
    print(s1.greet())  # Hello Ajay from ABC School
    ```

## 2. Class Method (@classmethod) (Works on class-wide data)

- First argument: cls → refers to the class
- Scope: Can access class variables and other class methods
- Use case: When method needs to work with class-level data or alternate constructors

    ```python 
    class Student:
        school = "ABC School"

        @classmethod
        def change_school(cls, new_school):
            cls.school = new_school

    Student.change_school("XYZ School")
    print(Student.school)  # XYZ School

    ```

## 3. Static Method (@staticmethod)  (Utility/helper functions)

- A method inside a class that does not take self or cls.
- Cannot access instance (self) or class (cls) variables.
- Essentially, it is a regular function grouped inside a class for logical organization. (Like a tax calculator function.)

    ```python
    class MathUtils:
        
        @staticmethod
        def add(a, b):
            return a + b

        @staticmethod
        def multiply(a, b):
            return a * b

    # Calling static methods from the class
    print(MathUtils.add(5, 3))       # 8
    print(MathUtils.multiply(4, 2))  # 8

    # Optional: calling from an instance
    m = MathUtils()
    print(m.add(10, 20))  # 30

    ```

# Python Shallow Copy vs Deep Copy
## What is Copying?

Copying creates a new object from an existing object. In Python, you can do shallow copy or deep copy.

### Shallow Copy

- Copies only the outer object.
- Inner objects (like nested lists) are shared, not copied.
- Fast, uses less memory
- Changes to inner objects affect the original

    ```python
    import copy

    library = [["Math", "Physics"], ["Novel", "Comics"]]

    # Shallow copy
    new_library = copy.copy(library)

    # Change a book in the first shelf
    new_library[0][0] = "Biology"

    print("Original:", library)      # [['Biology', 'Physics'], ['Novel', 'Comics']]
    print("Shallow:", new_library)   # [['Biology', 'Physics'], ['Novel', 'Comics']]
    ```

### Deep Copy

- Copies outer object AND all inner objects recursively.
- Fully independent, changes do not affect original
- Slower, uses more memory

    ```python
    import copy

    library = [["Math", "Physics"], ["Novel", "Comics"]]

    # Deep copy
    deep_library = copy.deepcopy(library)

    # Change a book in the first shelf
    deep_library[0][0] = "Chemistry"

    print("Original:", library)      # [['Math', 'Physics'], ['Novel', 'Comics']]
    print("Deep:", deep_library)     # [['Chemistry', 'Physics'], ['Novel', 'Comics']]
    ```

# str vs repr

## str

- Returns a human-readable representation of the object.
- Used when you call print(obj) or str(obj).

### Goal:

- To be readable and friendly for end users.

    ```python
    class Student:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return f"{self.name}, {self.age} years old"

    s = Student("Arun", 20)
    print(s)  # Output: Arun, 20 years old

    ```

## repr

- Returns an unambiguous string representation of the object.
- Used by repr(obj) or when you just type obj in a REPL.
- Helps debugging and recreating the object.

### Goal:

- To give developers a clear and reconstructable view of the object.

    ```python
    class Student:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __repr__(self):
            return f"Student(name='{self.name}', age={self.age})"

    s = Student("Arun", 20)
    repr(s)  # "Student(name='Arun', age=20)"

    ```

# Lists

- A list is a mutable, ordered collection of heterogeneous items in Python.

## Questions: 

1. Reverse a list without using reverse() or slicing?
    ```python
    nums = [1, 2, 3, 4, 5]
    reversed_list = []

    for i in range(len(nums)-1, -1, -1):
        reversed_list.append(nums[i])

    print(reversed_list)  # [5, 4, 3, 2, 1]
    ```

2. Remove duplicates.
    ```python
    nums = [1, 2, 2, 3, 4, 3, 5]
    unique = []
    seen = set()

    for x in nums:
        if x not in seen:
            unique.append(x)
            seen.add(x)

    print(unique)  # [1, 2, 3, 4, 5]
    ```
3. Flatten a nested list

    ```python
    nested = [[1,2],[3,4],[5,6]]
    flat = []
    for sublist in nested:
        for item in sublist:
            flat.append(item)
    print(flat)  # [1,2,3,4,5,6]
    ```

4. Merge two sorted lists without using sort()
    ```python
    a = [1,3,5]
    b = [2,4,6]
    merged = []
    i=j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]: merged.append(a[i]); i+=1
        else: merged.append(b[j]); j+=1
    merged.extend(a[i:]); merged.extend(b[j:])
    print(merged)  # [1,2,3,4,5,6]

    ```

5. Rotate a list by k positions
    ```python
    nums = [1,2,3,4,5]; k=2
    rotated = nums[-k:] + nums[:-k]
    print(rotated)  # [4,5,1,2,3]
    ```

6. Count frequency of elements in a list
    ```python
    nums = [1,2,2,3,1,2]
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    print(freq)  # {1: 2, 2: 3, 3: 1}
    ```

    ```python
    from collections import Counter
    nums = [1,2,2,3,1,2]
    n = Counter(nums)
    print(n[2]) #3
    ```

----

# Dictionaries

## What is a Dictionary?

- A dictionary is an unordered, mutable collection of key-value pairs in Python.
- Keys are unique and immutable (str, int, tuple, etc.)
- Values can be any data type and can be duplicated

    ```python

    student = {
        "name": "Ajay",
        "age": 20,
        "city": "Pune"
    }
    ```

### common methods

| Method                    | Description                                    |
| ------------------------- | ---------------------------------------------- |
| `dict.keys()`             | Returns a view of keys                         |
| `dict.values()`           | Returns a view of values                       |
| `dict.items()`            | Returns a view of key-value pairs              |
| `dict.get(key, default)`  | Returns value for key or default               |
| `dict.update(other_dict)` | Merge/update dictionary                        |
| `dict.pop(key)`           | Remove and return value of key                 |
| `dict.popitem()`          | Remove and return last inserted key-value pair |
| `dict.clear()`            | Remove all items                               |
| `dict.copy()`             | Shallow copy of dict                           |


### Questions

1. Merge two dictionaries without using update()

    ```python
    a = {"x": 1, "y": 2}
    b = {"y": 3, "z": 4}
    merged = {**a, **b}  # b overwrites a
    print(merged)  # {'x': 1, 'y': 3, 'z': 4}
    ```

2. Iterate over keys, values, and items

    ```python
    for key in student.keys(): print(key)
    for value in student.values(): print(value)
    for k,v in student.items(): print(k, v)

    ```

# Tuple

## What is a Tuple?

- A tuple is an ordered, immutable collection of elements in Python.

    ```python
    t = (1, 2, 3, "Python")
    print(t)  # (1, 2, 3, 'Python')

    ```

### Common Methods:
| Method              | Description                              |
| ------------------- | ---------------------------------------- |
| `count(x)`          | Returns number of times `x` appears      |
| `index(x)`          | Returns first index of `x`               |
| `len(t)`            | Returns number of elements               |
| `min(t)` / `max(t)` | Returns smallest/largest element         |
| `sum(t)`            | Returns sum of elements (numeric tuples) |


### Questions

1. Iterate over tuple and sum numeric elements?

    ```python
    t = (1, 2, 3, "Python", 4)
    total = 0
    for x in t:
        if isinstance(x, (int, float)):
            total += x
    print(total)  # 10

    ```

2. Unpack tuple into variables?

    ```python
    t = (1, 2, 3)
    a, b, c = t
    print(a, b, c)  # 1 2 3

    ```

---

# Python Sets

## What is a Set?

- A set is an unordered, mutable collection of unique elements in Python.

    ```python
    s = {1, 2, 3, 4, 2}
    print(s)  # {1, 2, 3, 4} → duplicates removed

    ```

### Common Methods
| Method                         | Description                                     |                      |
| ------------------------------ | ----------------------------------------------- | -------------------- |
| `add(x)`                       | Add element `x`                                 |                      |
| `remove(x)`                    | Remove element `x` (raises KeyError if missing) |                      |
| `discard(x)`                   | Remove element `x` (no error if missing)        |                      |
| `pop()`                        | Remove and return an arbitrary element          |                      |
| `clear()`                      | Remove all elements                             |                      |
| `union()` / `                  | Return union of sets                            |                      |
| `intersection()` / `&`         | Return intersection                             |                      |
| `difference()` / `-`           | Return difference                               |                      |
| `symmetric_difference()` / `^` | Elements in either set but not both             |                      |
| `issubset()` / `issuperset()`  | Check subset/superset                           |                      |


----

# Comprehensions

## List Comprehensions

### What is a List Comprehension?

- A list comprehension is a compact way to create lists using a single line of code.

#### Why List Comprehension?

- More concise and readable than traditional loops.
- Faster due to internal C-level optimisations and fewer operations.
- Reduces boilerplate code like append().
- Ideal for creating new lists from existing iterables efficiently.

#### Questions

1. Get the first letter of each word in a list.

    ```python
    words = ["apple", "banana", "cherry"]
    first_letters = [w[0] for w in words]
    print(first_letters)  # ['a', 'b', 'c']

    ```

2. Flatten a 2D list.
    ```python
    matrix = [[1, 2], [3, 4], [5, 6]]
    flattened = [x for row in matrix for x in row]
    print(flattened)  # [1, 2, 3, 4, 5, 6]

    ```

3. Extract vowels from a string.
    ```python
    text = "comprehension"
    vowels = [ch for ch in text if ch in 'aeiou']
    print(vowels)  # ['o', 'e', 'e', 'i', 'o']
    ```

4. Generate all combinations of letters from two lists.
    ```python
    a = ['A', 'B']
    b = ['X', 'Y']
    combinations = [x + y for x in a for y in b]
    print(combinations)  # ['AX', 'AY', 'BX', 'BY']

    ```

5. Find common elements in two lists.
    ```python
    a = [1, 2, 3, 4]
    b = [3, 4, 5, 6]
    common = [x for x in a if x in b]
    print(common)  # [3, 4]

    ```

6. Extract words starting and ending with same letter.
    ```python
    words = ["level", "apple", "madam", "test", "wow"]
    result = [w for w in words if w[0] == w[-1]]
    print(result)  # ['level', 'madam', 'wow']

    ```
## Dictionary Comprehension

### What is Dictionary Comprehension?

- Dictionary comprehension is a concise way to create dictionaries in Python using a single line of code.

#### WHY use Dictionary Comprehension?

- Cleaner code – No need for loops and dict() calls.
- Faster execution – Runs faster than for loops (optimised C implementation).
- Better readability – Express logic in one place.
- Easy filtering/transformation – Modify or filter key-value pairs in one go.

#### Questions
1. Swap keys and values.

    ```python
    data = {"a": 1, "b": 2, "c": 3}
    swapped = {v: k for k, v in data.items()}
    print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}
    ```

2. Create dictionary from two lists
    ```python
    keys = ['a', 'b', 'c']
    vals = [1, 2, 3]
    d = {k: v for k, v in zip(keys, vals)}
    print(d)  # {'a': 1, 'b': 2, 'c': 3}
    ```

3. Create dict with index as key and word as value
    ```python
    words = ["apple", "banana", "cherry"]
    indexed = {i: w for i, w in enumerate(words)}
    print(indexed)  # {0: 'apple', 1: 'banana', 2: 'cherry'}
    ```

4. Filter only even numbers from 1–10 and store number:square.

    ```python
    evens = {x: x**2 for x in range(1, 11) if x % 2 == 0}
    print(evens)  # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
    ```

5. Convert keys to uppercase.
    ```python
    data = {'name': 'Alice', 'city': 'Paris'}
    upper = {k.upper(): v for k, v in data.items()}
    print(upper)  # {'NAME': 'Alice', 'CITY': 'Paris'}
    ```

---

# map, filter, reduce

## What is map()?

- map() is a built-in function that applies a given function to each item of an iterable (like a list, tuple, etc.) and returns a map object (iterator).

### WHY use map()?

- Avoids manual loops → more concise and readable.
- Functional style → separates what you want to do from how.
- Efficient → returns an iterator, not a list (lazy evaluation).

#### Questions:
1. Convert list of words to uppercase

    ```python
    words = ["apple", "banana", "cherry"]
    result = list(map(str.upper, words))
    print(result)  # ['APPLE', 'BANANA', 'CHERRY']
    ```

2. Calculate factorial of each number inside list.

    ```python
    def fact(n):
        mul = 1
        for i in range(2, n + 1):
            mul *= i
        return mul


    l = [3, 4, 5, 6, 7, 8]
    print(list(map(fact, l))) #[6, 24, 120, 720, 5040, 40320]
    ```

3. Check if Numbers are Even

    ```python
    l = [123, 4, 3, 57, 657, 65, 6, 344, 12, 23, 2, 5, 7, 678, 67, 857, 45, 233]
    print(list(map(lambda x: True if x % 2 == 0 else False, l))) #[False, True, False, False]
    ```

4. Extract second element from each tuple
    ```python
    data = [(1, 'a'), (2, 'b'), (3, 'c')]
    result = list(map(lambda x: x[1], data))
    print(result)  # ['a', 'b', 'c']

    ```

5. Extract keys from list of dictionaries.
    ```python
    data = [{'a':1}, {'b':2}, {'c':3}]
    result = list(map(lambda d: list(d.keys())[0], data))
    print(result)  # ['a', 'b', 'c']
    ```
6. Reverse each string in a list

    ```python
    words = ['python', 'java']
    result = list(map(lambda x: x[::-1], words))
    print(result)  # ['nohtyp', 'avaj']
    ```

## What is filter()?

- filter(function, iterable)
- It filters (selects) elements from an iterable based on a condition defined in the function.
- Returns an iterator containing only elements for which the function returns True.

### WHY use filter()?

- Clean & readable – No need to write loops with if conditions.
- Efficient – Evaluates lazily (returns iterator, not list).
- Functional style – Works well with lambda and pure functions.
- Reusable logic – You can pass any function to define custom filtering conditions.

### Questions
1. Filter even numbers.

    ```python
    nums = [1, 2, 3, 4, 5, 6]
    result = list(filter(lambda x: x % 2 == 0, nums))
    print(result)  # [2, 4, 6]
    ```

2. Filter positive numbers.
    ```python
    nums = [-2, 0, 3, -5, 8]
    result = list(filter(lambda x: x > 0, nums))
    print(result)  # [3, 8]
    ````

3. Filter Prime Numbers.

    ```python
        l = [x for x in range(52)]


        def is_prime(n):
            m = math.floor(n / 2)
            flag = 1
            if n > 1:
                for i in range(2, m + 1):
                    if n % i == 0:
                        flag = 0
                        break
                if flag == 1:
                    return n
                else:
                    return None


        print(list(filter(is_prime, l)))

4. Filter words longer than 4 characters

    ```python
    words = ['cat', 'horse', 'dog', 'elephant']
    result = list(filter(lambda x: len(x) > 4, words))
    print(result)  # ['horse', 'elephant']
    ```

## What is reduce()?

- It applies a function cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value.
- Unlike map() and filter(), it returns a single result, not a list.

### WHY use reduce()?

- Clean and concise – Useful for cumulative operations like sum, product, or any combination.
- Functional programming style – Avoids explicit loops.
- Custom aggregations – Can apply any function to reduce elements.

### Questions.
1. Sum of all numbers in a list
    ```python
    from functools import reduce
    nums = [1, 2, 3, 4]
    result = reduce(lambda x, y: x + y, nums)
    print(result)  # 10
    ```

2. Concatenate strings
    ```python
    l = [
        "hello",
        "how",
        "are",
        "i",
        "am",
        "fine",
        "what",
        "about",
        "you",
        "nice",
        "to",
        "meet",
        "you",
    ]
    print(reduce(lambda a, b: a + b, l))
    ```
----

# Memory Management in Python

- Python handles memory automatically, so you don’t have to manually allocate or free it (like in C or C++).
- It uses two main techniques:

## Reference Counting

- Every object in Python has a reference count (how many variables refer to it).
- When the count becomes 0, the object’s memory is freed immediately.

    ```python
    import sys

    a = [1, 2, 3]
    print(sys.getrefcount(a))
    b = a
    print(sys.getrefcount(a))
    del a
    del b

## Garbage Collection (gc module)

- Reference counting can’t handle circular references (e.g. two objects referring to each other).
- The garbage collector periodically finds and deletes such cycles.

    ```python
    import gc

    class Node:
        def __init__(self):
            self.ref = None

    a = Node()
    b = Node()
    a.ref = b
    b.ref = a  # circular reference

    del a
    del b
    gc.collect()  # Garbage collector cleans up the cycle

-----

# Exception Handling

- An exception is an error that occurs during program execution (runtime).
- Exception handling lets you gracefully handle errors without crashing your program.

    Example: 
    ```python
        try:
            num = int(input("Enter a number: "))
            print(10 / num)
        except ValueError:
            print("Invalid number.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        except Exception as e:
            print("Unknown error:", e)

## Exception handling uses 4 main blocks

| Block     | Purpose       | Runs When            |
| --------- | ------------- | -------------------- |
| `try`     | Code to test  | Always               |
| `except`  | Handle errors | When an error occurs |
| `else`    | Success code  | When no error        |
| `finally` | Cleanup code  | Always               |

- Example:
    ```python
        try:
            x = int(input("Enter number: "))
        except ValueError:
            print("Invalid number")
        else:
            print("You entered:", x)
        finally:
            print("End of program")

---------

# Custom Exceptions

- Custom exceptions are user-defined error classes that allow you to handle specific scenarios not covered by built-in exceptions.

## Why Use Custom Exceptions?

- To represent business logic errors clearly
- To provide meaningful error messages
- To separate application-specific exceptions from system ones

### How to Create a Custom Exception

- You define a class that inherits from Python’s built-in **Exception** class.

### Custom Exception Example: Bank Withdrawal

- You’re building a bank system. If a user tries to withdraw more than their balance, instead of raising a generic **ValueError**, you raise a custom **InsufficientFundsError**.

    ```python
    class InsufficientFundsError(Exception):
        """Raised when withdrawal amount exceeds balance"""
        def __init__(self, balance, amount):
            self.balance = balance
            self.amount = amount
            self.message = f"Cannot withdraw {amount}. Available balance: {balance}"
            super().__init__(self.message)


    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self.balance = balance

        def deposit(self, amount):
            self.balance += amount
            return self.balance

        def withdraw(self, amount):
            if amount > self.balance:
                raise InsufficientFundsError(self.balance, amount)
            self.balance -= amount
            return self.balance


    # -------------------------
    # ✅ Usage
    try:
        account = BankAccount("Ajay", 1000)
        account.withdraw(1500)
    except InsufficientFundsError as e:
        print("Transaction Failed:", e)
    ```

-------------

# Threading in Python

## What is Threading?

- Threading allows you to run multiple parts of a program (threads) concurrently — useful when your program performs I/O-bound tasks (like network calls, file reading, etc).
- A thread is a lightweight unit of a process.

### Why Use Threading?

- To speed up I/O-bound operations
- To perform multiple tasks simultaneously
- To keep your program responsive

- Example: 

    ```python
    import time
    import threading

    def task1():
        for i in range(3):
            print("Task 1 running...")
            time.sleep(1)

    def task2():
        for i in range(3):
            print("Task 2 running...")
            time.sleep(1)

    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All done!")

## Factors influencing thread execution

1. Operating System Scheduler

    - Once you call t1.start(), the OS thread scheduler decides which thread runs first.
    - The scheduler considers:
        - CPU core availability
        - Thread priority (all Python threads have equal priority by default)
        - Current system load
        - Fairness algorithms (e.g., Round Robin, Priority Scheduling, etc.)
    - This is the biggest reason execution order is unpredictable.

2. Global Interpreter Lock (GIL)

    - Python (CPython) has a GIL, which allows only one thread to execute Python bytecode at a time.
    - Even on a multi-core CPU, Python threads take turns.
    - The GIL is periodically released (e.g., every few milliseconds or bytecode instructions).
    - This leads to context switching (jumping between threads), creating interleaved outputs.

3. Context Switching

    - Threads can be paused and resumed at any time by the OS.
    - Example: While t1 is running, the OS may pause it after 1 iteration and give CPU to t2.
    - The switching point is unpredictable.

4. Thread Start Timing

    - Even though you write t1.start() first, the start call only requests the OS to run it.
    - The OS may not schedule it immediately — it could run t2 first.
    - So "start order" ≠ "execution order".

5. I/O and Sleep

    - When a thread calls time.sleep() or waits for I/O (file, network), the OS suspends it and lets other threads run.
    - This is why in your code with sleep(1), the threads nicely interleave.
    - Without sleep, one thread could hog the CPU for longer.

6. Number of CPU Cores

    - If you have multiple cores, the OS can run Python threads on different cores.
    - But because of the GIL, only one thread runs Python code at a time — though C extensions (like NumPy) may bypass this.


# Multiprocessing in Python
## What is Multiprocessing?

- In Python, a process is an independent program running in its own memory space.
- Multiprocessing allows you to run multiple processes at the same time, so CPU-bound tasks can truly run in parallel.
- Each process runs independently, so they don’t share memory by default.
- Example
    ```python
    from multiprocessing import Process

    # Function to calculate squares
    def calc_square(numbers):
        for n in numbers:
            print(f"Square of {n} is {n*n}")

    if __name__ == "__main__":
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]

        # Create two processes
        p1 = Process(target=calc_square, args=(nums1,))
        p2 = Process(target=calc_square, args=(nums2,))

        # Start the processes
        p1.start()
        p2.start()

        # Wait for both to finish
        p1.join()
        p2.join()

        print("Done!")


## Multi threading vs Multi processing
| Feature                           | Multithreading                                                                          | Multiprocessing                                      |
| --------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **Definition**                    | Multiple threads within a single process                                                | Multiple independent processes                       |
| **Memory**                        | Shared memory (threads can access same variables)                                       | Separate memory for each process                     |
| **GIL (Global Interpreter Lock)** | Only one thread executes Python bytecode at a time → CPU-bound tasks not truly parallel | No GIL restriction → CPU-bound tasks run in parallel |
| **Use Case**                      | I/O-bound tasks (networking, file operations)                                           | CPU-bound tasks (heavy computation)                  |
| **Creation Overhead**             | Lightweight, quick to create threads                                                    | Heavyweight, creating processes is slower            |
| **Crash Impact**                  | One thread crash may affect whole process                                               | One process crash usually does not affect others     |
| **Communication**                 | Easy, shared variables                                                                  | Harder, requires IPC (Queue, Pipe, Manager)          |
| **Execution**                     | Concurrent (pseudo-parallel for CPU-bound)                                              | True parallel execution on multiple cores            |

-------------

# 1. What is async?

- Async in Python is used to write asynchronous code, which allows your program to do other tasks while waiting for I/O operations (like network requests, file reads, or database calls) to complete.
- Regular (synchronous) Python blocks until a task finishes.
- Async lets you pause a function at certain points and let other tasks run.

| Keyword     | Purpose                                                     |
| ----------- | ----------------------------------------------------------- |
| `async def` | Define an **asynchronous function** (coroutine)             |
| `await`     | Wait for another coroutine to complete **without blocking** |

- Exapmle:
    ```python
        import asyncio

        async def say_hello():
            print("Hello")
            await asyncio.sleep(2)  # non-blocking sleep
            print("World")

        async def main():
            await say_hello()
            print("Done")

        # Run the event loop
        asyncio.run(main())

    OUTPUT:
        Hello
        World
        Done


-------------

# Coding questions.

1. Compress a string (e.g., "aaabbc" → "a3b2c1")
    ```python
    s = "aaabbc"
    res = ""
    i = 0
    while i < len(s):
        count = 1
        while i+1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        res += s[i] + str(count)
        i += 1
    print(res)  # Output: a3b2c1
    ```

2. Check if two strings are anagrams
    ```python
    from collections import Counter
    s1, s2 = "listen", "silent"
    print(Counter(s1) == Counter(s2))  # Output: True

3. Longest common prefix among a list of strings

    ```python
    strs = ["flower","flow","flight"]
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    print(prefix)  # Output: "fl"

4. First non-repeating character

    ```python
    s = "swiss"
    from collections import Counter
    freq = Counter(s)
    for i,c in enumerate(s):
        if freq[c] == 1:
            print(i,c)  # Output: 0 s
            break


5. Second largest element

    ```python
    nums = [1,5,3,9,7]
    unique = list(set(nums))
    unique.sort()
    print(unique[-2])  # Output: 7



6. Pyramid of *

    ```python
        n = 4
        for i in range(n):
            print(" "*(n-i-1) + "*"*(2*i+1))

7. Diamond of *

    ```python
    n = 4
    # Upper part
    for i in range(n):
        print(" "*(n-i-1) + "*"*(2*i+1))
    # Lower part
    for i in range(n-2, -1, -1):
        print(" "*(n-i-1) + "*"*(2*i+1))

8. Hollow Square

    ```python
    n = 4
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1 or j==0 or j==n-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

9. Hollow triangle
    ```python
    n = 4
    for i in range(1, n+1):
        for j in range(n-i):
            print(" ", end="")
        for j in range(1, 2*i):
            if j==1 or j==2*i-1 or i==n:
                print("*", end="")
            else:
                print(" ", end="")
        print()


10. sort string of list
    ```python
        s = ['a', "aa", '100', '200', 'python', '300.12', '400']
        # s = [21,34,23,243,5345,3]
        for _ in range(len(s)):
            for i in range(0, len(s)-1):
                if s[i] > s[i+1]:
                    s[i], s[i+1] = s[i+1], s[i]

        print(s)

# Confusing questions
1. ```python
    def add_item(item, lst=[]):
        lst.append(item)
        return lst

    print(add_item(1))
    print(add_item(2))

    OUTPUT: [1]
            [1, 2]

2. ```python
    a = [1, 2, 3]
    b = a
    b.append(4)
    print(a)

    OUTPUT: [1, 2, 3, 4]

3. ```python
    print(True + True + False)


4. ```python
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a == b, a is b)

    OUTPUT: True False

5. ```python
    d = {1: "a", True: "b", 1.0: "c"}
    print(d)
    
    OUTPUT: {1: 'c'}    


6. ```python
    for i in range(3):
        print(i)
    else:
        print("Done")

    OUTPUT: 0
            1
            2
            Done
    
7. ```python
    def func():
        print("Hi")

    result = func()
    print(result)

    OUTPUT: Hi
            None

8. ```python
        lst = [False, False, False, True, False]

        l = [x*100 for x in lst]
        print(l)

        OUTPUT:
        [0, 0, 0, 100, 0]
