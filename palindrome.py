

string = input("Enter a string to check if its a Palindrome : ")

def palindrome(p):
    return p == p[::-1]   #used x[::-1] default python function to reverse a string



print("Palindrome : ", palindrome(string))