# 🔁 `while` Loop in Python?
A `while` **loop** is used to **repeat a block of code as long as a condition is** `True`.<br/>
👉 The loop keeps running **until the condition becomes False**.
##
## 🔤 Syntax
```python
while condition:
    # code to repeat
```
- `condition` → must return `True` or `False`
- Identation is mandatory(4 spaces)
##
## ✅ Understanding
```python
i = 1

while i <= 5:
    print(i)
    i = i + 1
```
🔍 **How it works:**
1. `i = 1`
2. Check condition `i <= 5` → True
3. Print `i`
4. Increase `i`
5. Loop stops when `i` becomes 6
##
## ⚠️ Important: Avoid Infinite Loop
If you forget to update the condition, the loop will run forever.

❌ Example (Infinite Loop):
```python
i = 1
while i <= 5:
    print(i)
```
✔ Fix:
```python
i = i + 1
```
##
## ✅ Examples
### 🔄 Example 1: User Input Loop
```python
password = ""

while password != "Admin123":
    password = input("Enter Password: ")

print("Access Granted")
```
📌 Used in login systems.
##
### 🔢 Example 2: Count Items in a List
```python
fruits = ["apple", "banana", "mango"]
i = 0

while i < len(fruits):
    print(fruits[i])
    i = i + 1
```
