
string_1 = input("Enter string 1 : ")
string_2 = input("Enter string 2 : ")

def anagram(s1 , s2):
    if sorted(s1) == sorted(s2):    #sorting to take common
       return True
    else:
       return False

print(anagram(string_1, string_2))
