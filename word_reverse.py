def word_reverse(word):
    reverse_word = ""

    for letter in range(len(word)-1,-1,-1):
        reverse_word+=word[letter]
    return reverse_word 
    
print(word_reverse("Pineapple"))
