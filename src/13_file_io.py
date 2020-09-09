"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
# * https://www.w3schools.com/python/python_file_open.asp
f1 = open('foo.txt', 'r')

print(f1.read())

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# * https://www.w3schools.com/python/python_file_write.asp
# * \n creates new line

f2 = open('bar.txt', 'w')
f2.write("aysfegriuyhafsriuyhafsoi \n")
f2.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaa \n")
f2.write("oh no. \n")
f2.close()

f2 = open('bar.txt', 'r')
print(f2.read())