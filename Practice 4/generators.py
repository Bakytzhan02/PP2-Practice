# Practice 4 - Iterators and Generators

# 1. Using iter() and next()
numbers = [1, 2, 3, 4]
number_iterator = iter(numbers)

print(next(number_iterator))
print(next(number_iterator))

# 2. Loop through an iterator
fruits = ("apple", "banana", "cherry")
fruit_iterator = iter(fruits)

for fruit in fruit_iterator:
    print(fruit)

# 3. Create a custom iterator
class CountToFive:
    def __init__(self):
        self.number = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 5:
            current_number = self.number
            self.number += 1
            return current_number
        else:
            raise StopIteration

counter = CountToFive()

for value in counter:
    print(value)

# 4. Generator function with yield
def generate_numbers():
    for number in range(1, 6):
        yield number

for number in generate_numbers():
    print(number)

# 5. Generator expression
squares = (number * number for number in range(1, 6))

for square in squares:
    print(square)
