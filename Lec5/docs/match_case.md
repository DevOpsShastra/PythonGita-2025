# 🔷 `match case` in Python
`match case` compares a value against multiple patterns and executes the first matching case.

Before match case, Python developers often used:
- Long if–elif–else chains
- Dictionary-based dispatch logic
  
These became:<br/>
❌ Hard to read <br/>
❌ Error-prone <br/>
❌ Difficult to maintain <br/>

`match case` provides a clean, readable, and structured way to handle multiple conditions.
> Introduced in Python 3.10<br/>
> It is Python’s way of handling multiple conditions cleanly.
##
## 🔤 Syntax
```bash
match value:
    case pattern1:
        action
    case pattern2:
        action
    case _:
        default action
```
🔍 **How it works:**
1. Python evaluates the value in `match`
2. It compares it with each `case`
3. Matching stops at the **first match**
4. Executes the corresponding block
5. If no match → `case _` executes
##
## ✅ Examples
### 🔷 Example 1: Simple Menu Selection
```python
choice = 2

match choice:
    case 1:
        print("Add Product")
    case 2:
        print("View Product")
    case 3:
        print("Delete Product")
    case _:
        print("Invalid choice")
```
🧠 How it works <br/>
- Python checks `choice`
- Matches it with each `case`
- Executes the matching block
- Stops after first match
##
### 🔷 Example 2: Calculator
```python
operation = "+"

match operation:
    case "+":
        print("Addition selected")
    case "-":
        print("Subtraction selected")
    case "*":
        print("Multiplication selected")
    case "/":
        print("Division selected")
    case _:
        print("Invalid operation")
```
- Easy to read
- Easy to add more operations
##
### 🔷 Example 3: Multiple Values in One Case
```python
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case _:
        print("Invalid day")
```
- `|` works like **OR**
##
### 🔷 Example 4: Matching Lists (Pattern Matching)
```python
data = [1, 2]

match data:
    case [1, 2]:
        print("Exact match")
    case [1, x]:
        print("Second value is", x)
    case _:
        print("No match")
```
