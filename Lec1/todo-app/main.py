# Welcome Message Section
print("-" * 100)
print(" " * 35, "Welcome to Todo Application")
print("-" * 100)


# User Input Section
user_prompt = "Enter a todo: "

todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3]


print(todos)
print("Total todo:", len(todos))
print(type(todos))
