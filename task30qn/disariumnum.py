

def is_disarium(number):
    #  number to a string 
    num_str = str(number)
    length = len(num_str)
    #  sum of digits each raised to the power of its position
    total_sum = sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str))
    return total_sum == number

number = 175
if is_disarium(number):
    print(f"{number} is a Disarium number.")
else:
    print(f"{number} is not a Disarium number.")