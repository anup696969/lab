a=input("Enter a sentence: ")
w=a.split(" ")
u= list(set(w))
print(f"The words are: {u}")
for words in u:
    print(words,w.count(words))