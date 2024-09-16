"""
  Team ID: 6
        Name                    ID
  Rahul Sanjay Panchal      1002147137
  Sejal Prithviraj Chavan   1002152342
  Ashritha varma pamudurthy 1002165358
  Harsha Potluri            1002162450
  
"""
# calculator.py
def add(x, y):
"""Addition"""
return x + y
def subtract(x, y):
"""Subtraction"""
return x - y
def multiply(x, y):
"""Multiplication"""
return x * y
def divide(x, y):
"""Division"""
if y == 0:
raise ValueError("Cannot divide by zero!")
return x / y
"""Square"""
def square(x, y):
  return x ** y
