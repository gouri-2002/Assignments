#create a function is_prime(num) to return true if the number is prime and false if the number not prime


def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
        else:
            return True
print(is_prime(4))
    

