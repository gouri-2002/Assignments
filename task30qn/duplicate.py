


lis=[2,3,4,5,6,6]

uni=[]
dup=[]

for ele in lis:
    if ele  not in uni:
        uni.append(ele)
    elif ele not in dup:
        dup.append(ele)

print(dup)
