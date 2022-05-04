print("enter 1st number")
number_1=int(input())

print("enter 2nd number")
number_2=int(input())

ex_or=number_1^number_2 #to know which bits are different as they will give output 1
bin_exor=bin(ex_or)
check_string=str(ex_or)

a=check_string.count("1")
print(a)