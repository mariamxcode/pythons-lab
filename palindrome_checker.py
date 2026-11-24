word = input("Enter word: ")
reverse_word = ""

for letter in range(len(word)-1,-1,-1):
    reverse_word+=word[letter]

if(word == reverse_word):
    print("It's a palindrome")
else:
    print("It's not a palindrome")
    

