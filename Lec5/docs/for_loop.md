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
##
# 🔢 `range()` in Python
`range()` is a built-in Python function used to generate a sequence of numbers.
##
## 🔤 Syntax
```python
range(start, stop, step)
```
📌 `start` and `step` are optional.
##
## ✅ Examples
### 🔷 Example 1 - range(stop) | One Parameter
```python
for i in range(5):
    print(i)
```
✔ Starts from `0`<br/>
✔ Stops at `4` (5 is excluded)
##
### 🔷 Example 2 - range(start, stop) | Two Parameter
```python
for i in range(1, 6):
    print(i)
```
✔ Starts from `1`<br/>
✔ Stops before `6`
##
### 🔷 Example 3 - range(start, stop, step) | Three Parameter
```python
for i in range(2, 11, 2):
    print(i)
```
✔ Starts from `2`<br/>
✔ Stops before `11`<br/>
✔ Step size = 2
