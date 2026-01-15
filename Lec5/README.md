# 📝 Todo Application (Python) - Lecture 5
A simple console-based Todo Application built using core Python concepts.

## 🗂️ Project Structure
```bash
PythonGita-2025/
├── Lec1
├── Lec2
├── Lec3
├── Lec5/
│   └── todo-app/
│       └── main.py  # Console-based Todo Application
│   ├── README.md    # Documentation for Lecture 4
```
##
## 🧾 Source Code
```python
print("-" * 100)
print(" " * 35, "Welcome to Todo Application")
print("-" * 100)

todos = []                                                 # Creates an empty list named todos

while True:                                                # Start an infinite loop
    user_action = input("Type add, view or exit: ")        # Prompt the user to choose an action

    match user_action:                                     # Matches the user input against predefined cases
        case "add":                                        # Executes when user types add
            todo = input("\nEnter a todo: ")                 # Takes a todo item from the user
            todos.append(todo)                               # Adds the todo item to the todos list
        case "view":                                       # Exexutes when user types view
            for item in todos:                               # Loops through each todo item
                print(item)                                  # Prints all stored todos one by one
        case "exit":                                       # Exexutes when user types exit
            break                                            # Breaks the infinite while loops

print("Bye-Bye!")                                          # Display a exit message(Executes after exiting loop)
```
##
## ▶️ Sample Output
```bash
----------------------------------------------------------------------------------------------------
                                   Welcome to Todo Application
----------------------------------------------------------------------------------------------------
Type add, view or exit: add

Enter a todo: Buy groceries
Type add, view or exit: add

Enter a todo: Complete Python assignment
Type add, view or exit: view
Buy groceries
Complete Python assignment
Type add, view or exit: add

Enter a todo: Go for a walk
Type add, view or exit: view
Buy groceries
Complete Python assignment
Go for a walk
Type add, view or exit: exit
Bye-Bye!
```
##
## 🎯 Key Learning Outcomes
This project helps you understand:
- How to build menu-driven programs
- How to store and retrieve data using lists
- Difference between infinite loops and controlled exit
- Clean decision handling using match-case
##
## 🔮 Future Understanding
- match case
- for loop
