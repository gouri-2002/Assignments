

# Input two numbers
num1 = 15
num2 = 20
gcd = num1
while num1 % gcd != 0 or num2 % gcd != 0:
    gcd -= 1

lcm = abs(num1 * num2) // gcd
print("The LCM of", num1, "and", num2, "is", lcm)