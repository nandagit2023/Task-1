


string = input("Enter a string : ")


def numchar(s):
    stlist = []          #create empty list
    for i in s:
        stlist.append(i)  #iterate the list using for loop and append each time

    return len(stlist)    #return length of the string using built in len function


print("Total number of words in the given string : ", numchar(string))