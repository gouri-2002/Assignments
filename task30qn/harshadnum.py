

n=int(input("enter the number"))
ans=0
num=n
while(n!=0):
    rem=n%10
    ans+=rem
    n=n//10
if num%ans==0:
    print("the number is a harshad number")
else:
    print("the number is not a harshad number")