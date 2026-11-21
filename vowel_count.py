def vowel_count(word):
    vowel_count = 0
    vowel_checker = ""
    vowel = "aeiouAEIOU"
    for letter in word:
        for character in vowel:
            if letter == character: 
                if  letter not in  vowel_checker:
                    vowel_checker+=character
                else:
                    continue
                vowel_count+=1
                    
    return vowel_count
print(vowel_count("minee"))
