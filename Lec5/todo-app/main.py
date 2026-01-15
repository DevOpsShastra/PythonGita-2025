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

