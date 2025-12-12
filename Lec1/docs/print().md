# print() Function

### :white_check_mark: a. What is `print()` in Python?
`print()` is a built-in Python function used to display output on the screen.

Example
```python
print("Hello World")
```

Output:
```nginx
Hello World
```
##
### :white_check_mark: b. `print()` with Parameters
`print()` can take one or more values separated by commas

**Example 1:** Multiple values
```python
print("Course Name:", "PythonGita")
```

Output:
```nginx
Course Name: PythonGita
```

**Example 2:** Using Variables
```python
name = "Virat Kholi"
century = 53
print("The Indian cricketer", name, "has", century, "centuries in ODI cricket.")
```

Output:
```nginx
The Indian cricketer Virat Kholi has 53 centuries in ODI cricket
```
Python automatically adds a space between parameters
##
### :white_check_mark: c. Print with Separator (`sep`)
When you print multiple values, Python inserts a **space by default**
```python
print("A", "B", "C")
```
Output:
```nginx
A B C
```
You can change the separator using `sep`
```python
print("A", "B", "C", sep="-")
```
Output:
```nginx
A-B-C
```
##
### :white_check_mark: d. Printing Number of Times
You can multiply a string to repeat it.
Example:
```python
print("*" * 5)
```

Output
```nginx
*****
```
