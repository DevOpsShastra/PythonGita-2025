# 🔁 `for` Loop in Python
A `for` loop is used to **repeat a block of code** for **each item in a sequence** such as:
- a list
- a string
- a range of numbers
  
Instead of writing the same code again and again, a `for` loop helps you **iterate** over data one by one.
##
## 🔤 Syntax
```python
for variable in sequence:
    statements
```
- `variable` → takes one value at a time
- `sequence` → list, string, or range
- Indentation is **mandatory**
##
## ✅ Examples
### 🔷 Example 1: Loop Through Numbers
```python
for i in range(1, 6):
    print(i)
```
- `range(1, 6)` generates numbers from 1 to 5.
##
### 🔷 Example 2: Loop Through a List
```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
```
##
### 🔷 Example 3: Loop Through a String
```python
for char in "Python":
    print(char)
```
##
### 🔷 Example 4: Calculate Sum of Numbers
```python
total = 0

for i in range(1, 6):
    total = total + i

print("Total:", total)
```
