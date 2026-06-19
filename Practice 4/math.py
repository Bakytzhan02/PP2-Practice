# Practice 4 - Math and Random Operations

import math
import random

# 1. Built-in math functions
numbers = [5, 10, 2, 8]

print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Absolute value:", abs(-15))
print("Rounded number:", round(3.75))
print("Power:", pow(2, 3))

# 2. math module functions
print("Square root:", math.sqrt(25))
print("Ceil:", math.ceil(4.2))
print("Floor:", math.floor(4.8))
print("Sin:", math.sin(math.pi / 2))
print("Cos:", math.cos(0))
print("Pi:", math.pi)
print("Euler number:", math.e)

# 3. random module
print("Random float:", random.random())
print("Random integer:", random.randint(1, 10))

fruits = ["apple", "banana", "cherry"]
print("Random choice:", random.choice(fruits))

random.shuffle(fruits)
print("Shuffled list:", fruits)
