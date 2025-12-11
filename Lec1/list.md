# List in Python
A **list** is an ordered collection of items/elements, which can be of **any data type** - integers, strings, floats, booleans or even other lists.
### ✔️ Key Characteristics 
| **Feature**             | **Explanation**                                  |
| :---------------        | :---------------                                 |
| **`Ordered`**           | Items maintain the order in which they are added |
| **`Mutable`**           | You can change, add or remove items              |
| **`Allows duplicates`** | Same value can appear multiple times             |
| **`Heterogeneous`**     | Can contain different data types                 |
##
### ✅ 1. How to create a List
```python
my_list = [10, 20, 30]
mixed_list = [10, "Apple", True, 3.14]
```
##
### ✅ 2. Accessing List Elements
Python uses **indexing**, starting from 0.
```python
numbers = [10, 20, 30, 40]

# Positive Indexing
print(numbers[0])    # 10
print(numbers[3])    # 40

# Negative Indexing
print(numbers[-1])   # 40
print(numbers[-2])   # 30
```
##
### ✅ 3. Adding Elements to a List
1. `append()` -> **adds items at the end**
```python
fruits = ["apple", "banana"]
fruits.append("mango")

print(fruits)     # ["apple", "banana", "mango"]
```
2. `insert()` -> **adds items at specific position**
```python
fruits.insert(1, "grapes")
print(fruits)     # ["apple", "grapes", "banana", "mango"]
```
3. `extend()` -> **add multiple items**
```python
fruits.extend(["orange", "kiwi"])
print(fruits)     # ["apple", "grapes", "banana", "mango", "orange", "kiwi"]
```
##
### ✅ 4. Changing List Items
```python
fruits[0] = "pineapple"
print(fruits)     # ["pineapple", "grapes", "banana", "mango", "orange", "kiwi"]
```
##
### ✅ 5. Removing Elements
1. `remove()` -> **remove by value**
```python
fruits.remove("banana")
print(fruits)     # ["pineapple", "grapes", "mango", "orange", "kiwi"]
```
2. `pop()` -> **remove by index or remove last element**
```python
# remove by index
fruits.pop(2)
print(fruits)     # ["pineapple", "grapes", "orange", "kiwi"]

# remove last element
fruits.pop()
print(fruits)     # ["pineapple", "grapes", "orange"]
```
3. `clear()` -> **clear entire list**
```python
fruits.clear()
print(fruits)     # []
```
##
### ✅ 6. Useful List Functions
```python
len(my_list)      # length
max(my_list)      # largest
min(my_list)      # smallest
sum(my_list)      # total
```
