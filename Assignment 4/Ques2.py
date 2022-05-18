year=int(input("enter the year : "))

if year%4==0:
    print("entered year is a leap year")
elif year%100==0 & year%400==0:
     print("entered year is a leap year")
else:
    print("entered year is not a leap year")