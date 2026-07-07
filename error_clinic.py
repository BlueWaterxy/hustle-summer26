# Snippet 1
# Can't divide by zero error
x = 10
y = 0
if y != 0:
    result = x / y
    print("Result:", result)
else:
    print("Cannot divide by zero")
# Snippet 2 
# Index error 
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    print(numbers[i])
# Snippet 3 
# Syntax error
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

radius = 5
print(calculate_area(radius))
# Snippet 4 
# Syntax error
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))
# snippet 5
# syntax error 
for i in range(5):
    print(i)
# snippet 6
# Syntax error
def greet(name):
    return "Hello, " + name

print(greet("Alice"))
# snippet 7
# IndentationError:
numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number

print("Sum of numbers:", total)
# snippet 8 
# LOGIC ERROR
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
# snippet 9
# Logic error 
name = input("Enter your name: ")

if name == "Alice" or name == "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")
# snippet 10
# ZeroDivisionError
def divide_numbers(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

num1 = 10
num2 = 0

print(divide_numbers(num1, num2))