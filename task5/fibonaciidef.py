#create a function is_fibonacii(num) to return true if the number is fibonacii and false if the number not fibonacii

def is_fibonaci(num):
    previous=0
    current=1
    
    if num in (0,1):
    
        next=previous+current
    
    while(next<=num):
        next=previous+current
        previous=current
        current=next
        
        if next==num:
            return True
        else:
            return False
print(is_fibonaci(56))

