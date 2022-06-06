up_range= int(input('Enter the upper range to find prime numbers till it : '))

for i in range(up_range):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)