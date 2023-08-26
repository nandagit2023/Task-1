

string = input ("Enter any String to Remove Vowels in it : ")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def remove_vowel(string):
    result = ""
    for i in range(len(string)):
        if string[i] not in vowels:
            result = result + string[i]
    return result

print("After removing vowels : ", remove_vowel(string))






