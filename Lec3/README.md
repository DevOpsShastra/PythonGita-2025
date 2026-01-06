# 📝 Todo Application (Python) - Lecture 3
A simple console-based Todo Application built using core Python concepts.

## 🗂️ Project Structure
```bash
PythonGita-2025/
├── Lec3/
│   └── todo-app/
│       └── main.py  # Console-based Todo Application
│   ├── README.md    # Documentation for Lecture 3
```
##
## 🧾 Source Code
```python
# Welcome Section
print("-" * 100)
print(" " * 35, "Welcome to Todo Application")
print("-" * 100)

user_prompt = "Enter a todo: "     # Store input message so it can be reused
todos = []                         # Creates an empty list to store todo items
counter = 0                        # Used to control how many times the loop runs

while counter < 3:                 # Ensures the loop runs until counter value is less then 3
    todo = input(user_prompt)      # Accepts user input from the keyboard
    todos.append(todo)             # Adds the entered todo to the list
    counter = counter + 1          # Increments the counter to avoid an infinite loop

print(todos)                       # Display all todo items entered by user
```
##
## ▶️ Sample Output
```bash
----------------------------------------------------------------------------------------------------
                                   Welcome to Todo Application
----------------------------------------------------------------------------------------------------
Enter a todo: Buy groceries
Enter a todo: Learn Python
Enter a todo: Exercise
['Buy groceries', 'Learn Python', 'Exercise']
```
##
## 🎯 Learning Objective
This project helps to understand:
- How loop work
- How list store data
- How user input is handled
- How programs grows from a small logic
##
## 🔮 Future Understanding
- while loop
