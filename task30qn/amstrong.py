numbers=[151,153,154,370,371,372,373,16341,1635]
for i in range(0,len(numbers)):
    total=0
original=numbers[i]
dig_count=len(str(numbers)) #to get the length in strings
while(numbers!=0):
    digit=numbers[i]%10
    exponent=digit**dig_count
    total=total+exponent
    numbers[i]=numbers[i]//10

if(original==total):
    print(f"{original} is a an amstrong number")
else:
    print(f"{original} is not an amstrong number")