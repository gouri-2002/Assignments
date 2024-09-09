

a=[8,24,56,44,567]
n=len(a)
minimum=a[0]
for m in range(1,n):
    if a[m]<minimum:
        minimum=a[m]
print("smallest element",minimum)