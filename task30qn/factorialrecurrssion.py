
def factorial(n):
    # factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n-1)
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")