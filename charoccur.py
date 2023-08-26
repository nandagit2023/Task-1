

string = input("Enter first string : ")


def uni_var (s):
    uni_list = []
    max_count = []
    for i in s:
        if i not in uni_list:
           uni_list.append(i)               #unique char list creation
           max_count.append(s.count(i))     #when loop iterates each char will be checked for max occ in same string and count taken - stored in list
    occ = max(max_count)                    #will max num from list created
    pos = uni_list[max_count.index(occ)]    #bytaking max count and getting the corresponding index from unique list
    return pos


print("Max occurred char in string : ", uni_var(string))