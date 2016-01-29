'''given two strings, determine how many times the second string, or an anagram of the second string, occurs in the first string'''



def count_anagrams(s1, s2):
    '''count number of items s2, or an anagram of s2, occurs in s1
    inputs: strings s1, s2
    output: int'''

    # sort s2
    sorted_str = ''.join(sorted(s2))

    # initialize count
    c = 0
    # loop over characters in s1
    for ix, char in enumerate(s1):
        # define substring of s1 that is the length of s2
        sub_str = s1[ix : ix+len(s2)]
        # count if the sorted substring is equal to sorted s2
        if ''.join(sorted(sub_str)) == sorted_str:
            c += 1

    return c

print count_anagrams('AbrAcadAbRa', 'cAda')
