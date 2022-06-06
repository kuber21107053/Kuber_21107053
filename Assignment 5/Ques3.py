a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  

if a<b+c and b<a+c and c<a+b:   
    s = (a + b + c) / 2  #semi-perimeter

    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
    print('The area of the triangle is: ',area)   