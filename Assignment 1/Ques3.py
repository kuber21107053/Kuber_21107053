print("enter number of seconds")
num_sec=int(input())

minutes= int(num_sec//60)
seconds= int(num_sec%60)
print (str(minutes) + " minutes and " + str(seconds)+ " seconds")