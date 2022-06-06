word_list=[]
n=int(input("enter the number of words: "))
for i in range(n):
    word=str(input("Enter the word: "))
    word_list.append(word)

for word in word_list:
    count= word_list.count(word)
    print(word," occurs ",count, " times")