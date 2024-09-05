

numbers=[10,11,12,13,14,20,21]

#print prime numbers

for i in range(0,len(numbers)):

    num=numbers[i]
    if num %i ==0 and num>2:
        print(numbers[i])