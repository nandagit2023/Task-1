


string_1 = "Guvi Geeks Network Private Limited"
count = 0
list_vowel = []

for i in string_1:
      if (i == 'a') or (i == 'e') or (i == 'i') or (i == 'o') or (i == 'u') or (i == 'A') or (i == 'E') or (i == 'I') or (i == 'O') or (i == 'U'):
            list_vowel.append(i)
            count = count + 1

print("Vowels in the given string : ", list_vowel)
print("Total number of vowels : ", count)
print("Occurrence of 'a' or 'A' : ", list_vowel.count('a' or 'A'))
print("Occurrence of 'e' or 'E' : ", list_vowel.count('e' or 'E'))
print("Occurrence of 'i' or 'I' : ", list_vowel.count('i' or 'I'))
print("Occurrence of 'o' or 'O' : ", list_vowel.count('o' or 'O'))
print("Occurrence of 'u' or 'U' : ", list_vowel.count('u' or 'U'))
