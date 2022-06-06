up_range=int(input("Enter upper range :"))
div_num=int(input("Enter the number that should be divided by..."))
for i in range(1,up_range):
    if i%div_num==0:
        print(i)