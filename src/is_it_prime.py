import sys

def isPrime(n):
    if n <= 3:
        print(n)
    elif n % 2 == 0 or n % 3 == 0:
        print(f"{n} is prime")

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            print(f"{n} is not prime")
        i = i + 6

    print(f"{n} is prime")

n = int(input("Enter a number to see if it is prime, or anything else to exit. > "))
isPrime(n)

# function is_prime(n)
#     if n ≤ 3 then
#         return n > 1
#     else if n mod 2 == 0 or n mod 3 == 0
#         return false

#     let i ← 5

#     while i × i ≤ n do
#         if n mod i = 0 or n mod (i + 2) = 0
#             return false
#         i ← i + 6

#     return true
