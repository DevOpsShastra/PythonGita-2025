print("-" * 100)
print(" " * 35, "Welcome to Todo Application")
print("-" * 100)

# User Input Section
user_prompt = "Enter a todo: "
todos = []

counter = 0

while counter < 3:
    todo = input(user_prompt)
    todos.append(todo)
    counter = counter + 1

print(todos)