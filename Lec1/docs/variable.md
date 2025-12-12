# :white_check_mark: 1. What is Variable in Python?
A variable is like a **container** or **box** that stores a value.<br />
You can change the value in the box anytime.

📌 In Python:
> You don't need to declare the type (Python detects it automatically)<br />
> A variable is created as soon as you assign a value.

Example:
```python
name = "Rohit Sharma"
age = 38
price = 99.5
```
- `name` stores text
- `age` stores a number
- `price` stores a decimal
You can use variables anytime in your program.
##
# :white_check_mark: 2. Variable Naming Rule
Python has specific rules for creating variable names:<br />
### :heavy_check_mark: Allowed:
- Must start with a letter or underscore <br />
Example: `name`, `_age`
- Can contain letters, numbers, underscores <br />
Example: `age1`, `student_name`
- Case-sensitive <br/>
`Name` ≠ `name`

### :x: Not allowed:
- Cannot start with a number <br />
:x: `1age`
- No special characters <br />
:x: `name!`, `price@`
- Cannot use Python keywords <br />
:x: `class`, `for`, `if` as variable name

### Good practice:
- Use meaningful names <br />
✔️ `total_marks` <br />
✔️ `city_name`
