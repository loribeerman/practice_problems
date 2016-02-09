def str_shuffle(str1, str2, str3):
    '''determine if str3 is a valid shuffle of str1 and str2'''

    l1 = []
    l2 = []
    for char in str3:
        if char in str1:
            l1.append(char)
        if char in str2:
            l2.append(char)

    return (''.join(l1) == str1) and (''.join(l2) == str2)

str1="abc"
str2="def"
str3="dabecf"

print str_shuffle(str1, str2, str3)
