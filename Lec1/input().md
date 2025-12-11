# :white_check_mark: 1. `input()` in Python
`input()` is used to take data from the user.

**Example:**
```python
name = input("Enter your name: ")
```
- Python waits for rhe user to type something
- The value is stored in the variable
- `input()` **always return a string**

**Example:**
```python
age = input("Enter your age: ")
print("You are", age, "years old")
```
##
# ✅ 2. `Data Types` in Python
A data type tells Python **what kind of value** a variable is storing.
### 📌 Summary Table

| Data Type       | Example         | Description     |
| --------------- | --------------- | --------------- |
| `str`           | "Hello"         | Text            |
| `int`           |	10              | Whole numbers   |
| `float`  	      | 10.5            | Decimal numbers |
| `bool`	        | True            | Logical values  |
| `list`	        | [1, 2, 3]	      | Ordered, changeable |
| `tuple`	        | (1, 2, 3)       |	Ordered, unchangeable |
| `dict`          |	{"a": 1}        |	Key-value pairs |
| `set`	          | {1, 2, 3}       |	Unique items    |
##
# ✅ 3. `type()` in Python
`type()` is a built-in Python function used to **check the data type of any variable or value** <br />

**Example:**
```python
name = "Rahul Dravid"
age = 50
price = 99.5
is_active = True

print(type(name))
print(type(age))
print(type(price))
print(type(is_active))
```

**Output:**
```nginx
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```
##
# ✅ 4. `len()` in Python
`len()` is a built-in function that returns the **length**.
```python
# with string
name = "Mahendra Singh Dhoni"
print(len(name))    # Output: 20

# with list
fruits = ["apple", "banana", "mango"]
print(len(fruits))  # Output: 3
```
