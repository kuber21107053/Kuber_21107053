a_list=[]
for i in range(10):
    list_num=int(input("enter the number: "))
    a_list.append(list_num)
print(a_list)

#part a:- (print +ve numbers)
for num in a_list:
    if num>0:
        print(num," is a positive number")
              
#part b:- (print -ve numbers)
for num in a_list:
    if num<0:
             print (num,'is a negative number')
#part c:- (print odd numbers)
for num in a_list:
    if num%2!=0:
                print (num,'is a odd number')
#part d:- (print even numbers)
for num in a_list:
    if num%2==0:
               print(num, 'is a even number')
#part e- (print number of times each number occuring the list)
for num in a_list:
    count=a_list. count (num)
    print (num,'occurs', count," times")
