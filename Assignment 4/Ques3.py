import random

i=0
while i<10:
    num1=random.randint(0,10)
    num2=random.randint(0,10)
    
    print("Ques ",i+1)
    print("solve {} * {} =".format(num1,num2))
    ans=int(input("enter your answer : "))
    
    if ans==num1*num2:
        print("Right")
    else:
        print("Wrong. The answer is {}".format(num1*num2))
    i+=1
    print("**********")
