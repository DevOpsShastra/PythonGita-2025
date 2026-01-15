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
'''python
print("-" * 100)
print(" " * 35, "Welcome to Todo Application")
print("-" * 100)

todos = []

while True:
    user_action = input("Type add, view or exit: ")

    match user_action:
        case 'add':
            todo = input("\nEnter a todo: ")
            todos.append(todo)
        case 'view':
            for item in todos:
                print(item)
        case 'exit':
            break

print("Bye-Bye!")
'''

