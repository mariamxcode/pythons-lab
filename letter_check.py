word = input("Enter word: ")
vowel = "aeiouAEIOU"
vowel_count=0
consonant_count=0
for letter in range(65,92):
     if chr(letter) in word:
        for char in vowel:
            if chr(letter)==char:
                vowel_count+=1
        consonant_count+=1
        
for letter in range(97,123):
     if chr(letter) in word:
        for char in vowel:
            if chr(letter)==char:
                vowel_count+=1
        consonant_count+=1     


print("Vowel: ",vowel_count)
print("Consonant: ",consonant_count)

