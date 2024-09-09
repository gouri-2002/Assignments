

a=[8,24,56,44,567]
n=len(a)
maximum=a[0]
for m in range(1,n):
    if a[m]>maximum:
        maximum=a[m]
print("largest element",maximum)