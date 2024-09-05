

def is_palindrome(num):
    
    
    result=0

while(num!=0):

    digit=num%10

    result=result*10+digit

    num=num//10

print(is_palindrome(121))