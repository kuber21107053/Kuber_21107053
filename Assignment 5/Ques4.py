n=5
for i in range(n):          #for upward triangle
    for j in range(i+1):
        print("*", end=" ")
    print()

for i in range(n-1):        #for downward triangle
    for j in range (n-1-i):
        print("*", end=" ")
    print()
