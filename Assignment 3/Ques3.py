import math
#a
print((3+4)*5)

#b
n = int(input("Enter Number"))
ans = (n*(n-1))/2
print(ans)

#c
r = int(input("Enter Number"))
m = 4*math.pi*(r**2)        
print(m)

#d
r_1 = int(input("Enter Number"))
a = int(input("Enter Angle in degrees for cos"))
b=int(input("Enter Angle in degrees for sin"))
c = math.cos(a*math.pi/180)**2
d = math.sin(b*math.pi/180)**2
answ = (r_1*c + r_1*d)**0.5
print(answ)

#e
y1 = int(input("Enter Number y1"))
y2 = int(input("Enter Number y2"))
x1 = int(input("Enter Number x1"))
x2 = int(input("Enter Number x2"))
ansr = (y1 - y2)/(x1 - x2)
print(ansr)
