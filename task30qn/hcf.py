

def find_hcf(a, b):
    while(b):
        a, b = b, a % b
    return a
num1 = 10
num2 = 80
hcf = find_hcf(num1, num2)
print(f"The HCF of {num1} and {num2} is {hcf}")