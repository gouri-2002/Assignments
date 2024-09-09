

text=input("enter the text")
d={"upper_case":0 ,"lowercase":0}
for c in text:
    if c.isupper():
        d["upper_case"]+=1
    elif c.islower():
        d["lowercase"]+=1
    else:
        pass

print("upper count:",+d["upper_case"])
print("lower count:",+d["lowercase"])