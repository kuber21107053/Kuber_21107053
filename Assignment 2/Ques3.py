a=56
b=10

x=a&b
print("a&b = "+ str(x))

y=a|b
print("a|b = "+ str(y))

z=a^b
print("a^b = "+ str(z))

l_shift1=a<<2 #left shift a with 2 bits
l_shift2=b<<2 #left shift b with 2 bits
print("left shifting a with 2 bits = "+ str(l_shift1) + "\nleft shifting b with 2 bits = "+ str(l_shift2))

r_shift1=a>>2 #right shift a with 2 bits
r_shift2=b>>2 #right shift b with 2 bits
print("right shifting a with 2 bits = "+ str(r_shift1) + "\nright shifting b with 2 bits = "+ str(r_shift2))