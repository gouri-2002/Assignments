weight=int(input("enter the weight"))
height=int(input("enter the height"))

height_in_m2=height/100
bmi=weight/height_in_m2**2
print(f"bmi={bmi}")

if bmi<=19:
    print("under weight")
elif bmi<=25:
    print("normal weight")
elif bmi<=30:
    print("over weight")
else:
    print("obese")
            