
word = input("Enter word: ")
sorted_word = " "

for letter in range(len(word)):
     if(letter % 2 == 0):
        sorted_word+=word[letter]
     


print("New Word: ",sorted_word)

