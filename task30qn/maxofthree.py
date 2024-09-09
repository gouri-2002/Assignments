

frst=int(input("enter the first number"))
secnd=int(input("enter the second number"))
thrd=int(input("enter the third number"))

def find_max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c  

print("the largest number is",find_max(frst,secnd,thrd)) 