# PYTHON CHEATSHEET - Lecture 1

This cheatsheet is **clean, beginner-friendly explanation** of today's lecture topics.

```python
# ----------------------------------------------------------------------------------
# Welcome Message Section
# ----------------------------------------------------------------------------------

# Prints a line made of 100 hyphens ("-") to create a visual separator
print("-" * 100)

# Prints spaces to center the text visually, followed by the welcome message
print(" " * 35, "Welcome to Todo Application")

# Prints another line of 100 hyphens to close the header section
print("-" * 100)


# ----------------------------------------------------------------------------------
# User Input Section
# ----------------------------------------------------------------------------------

# This message will be shown each time the user is asked to enter a todo item
user_prompt = "Enter a todo: "

# Asking user for three todo items (one by one)
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)


# ----------------------------------------------------------------------------------
# Store Todos in a List
# ----------------------------------------------------------------------------------

# A list is a collection that can store multiple values
todos = [todo1, todo2, todo3]


# ----------------------------------------------------------------------------------
# Output Section
# ----------------------------------------------------------------------------------

# Print the complete list of todos entered by the user
print(todos)

# Print how many todo items are stored in the list using len() function
print("Total todo:", len(todos))

# Print the type of the variable 'todos' (it will show <class 'list'>)
print(type(todos))

```
##

## :rocket: Understanding
> [print() Function]()<br />
> [variables]()<br />
> [input(), data type, type(), len()]()<br />
> [list]()<br />
