"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print("printf operator (%): " +
      "%s is 10, %s is 2.25, %s is I like turtles!" % (x, y, z))
print("----")

# * %s - String (or any object with a string representation, like numbers)

# * %d - Integers

# * %f - Floating point numbers

# * %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# * %x/%X - Integers in hex representation (lowercase/uppercase)

# Use the 'format' string method to print the same thing

txt1 = "{} is 10, {} is 2.25, {} is I like turtles!".format(x, y, z)

print(f"format string method: {txt1}")
print("----")

# Finally, print the same thing using an f-string

print(f"f-string: {x} is 10, {y} is 2.25, {z} is I like turtles!")
print("----")
