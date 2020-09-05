"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 

Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""
# * Syntax for List Comprehension: [expression for item in list]

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [number for number in range(1, 6)]

print(f"Expected Outcome: [1, 2, 3, 4, 5]")
print(f"Got: {y}")
print("----")

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [number ** 3 for number in range(10)]

print(f"Expected Outcome: [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]")
print(f"Got: {y}")
print("----")

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [word.upper() for word in a]

print(f"Expected Outcome: ['FOO', 'BAR'', 'BAZ']")
print(f"Got: {y}")
print("----")

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [number for number in x if int(number) % 2 == 0]

print(f"Expected Outcome: Only Even Ints")
print(f"Got: {y}")
