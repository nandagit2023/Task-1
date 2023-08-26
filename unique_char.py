
string = input ("Enter any String to print unique chars : ")

def unique_char(u):
    unique_finds = set(u)    # I have used inbuilt set functions to find unique char
    return unique_finds

print(unique_char(string))
