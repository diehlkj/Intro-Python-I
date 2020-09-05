# Write a function is_even that will return true if the passed-in number is even.
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

print(f"2 should be an even number: {is_even(2)}")
print(f"1 should be an odd number: {is_even(1)}")
print("\n")


# Read a number from the keyboard
# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE

def enterNumber():
    print("Enter a number, or 'q' to exit:")
    num = input("> ")

    try:
        num = int(num)
        if num % 2 == 0:
            print("\n")
            print(f"{num} is Even")
            print("\n")
        else:
            print("\n")
            print(f"{num} is Odd")
            print("\n")
    except ValueError:
        try:
            num = float(num)
            print("\n")
            print(f"{num} is not even or odd. It is a float")
            print("\n")
        except ValueError:
            if num == "q" or num == "Q":
                return
            else:
                print("\n")
                print(f"'{num}' is not a number. It is a string.")
                print("\n")
    enterNumber()


enterNumber()