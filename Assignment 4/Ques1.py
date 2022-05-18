marks=int(input("Enter your marks : "))

if marks> 80:
    print("Your grade is A")
elif marks>60 & marks<=80:
    print("Your grade is B")
elif marks>50 & marks<=60:
    print("Your grade is C")
elif marks>45 & marks<=50:
    print("Your grade is D")
elif marks>25 & marks<=45:
    print("Your grade is E")
else:
    print("Your grade is F")