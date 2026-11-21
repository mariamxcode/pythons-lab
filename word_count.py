word = input("Enter the word: ")
def word_count(word):
    count = 0;
    for letters in word:
        count+=1
    return count
