from collections import defaultdict
import numpy as np

'''find cosine similarities of two strings of text'''


def str_split(text):
    '''split string of text into words'''
    return text.split(' ')


def word_counts(words):
    '''take list of words and return dict of word counts'''
    d = defaultdict(int)
    for word in words:
        d[word] += 1

    return d


def vector_magnitude(d):
    '''calculate magnitude of a vector where the vector is the dict values
    output: float'''

    return np.sqrt(sum([num**2 for num in d.values()]))


def cosine_sim(d1, d2):
    '''calculate cosine similarity of two vectors
    input: dictionaries, where the keys are the words and values are the count
    output: float'''

    # get dot product of vectors where the word is in both dicts
    prod = []
    for word in list(set(d1.keys()) & set(d2.keys())):
        prod.append(d1[word] * d2[word])
    dot_prod = sum(prod)

    # calculate magnitude of vectors
    d1_mag = vector_magnitude(d1)
    d2_mag = vector_magnitude(d2)

    # cosine similarity
    return dot_prod / (d1_mag * d2_mag)



A = 'the cat in the hat'
B = 'the red cat'
d1 = word_counts(str_split(A))
d2 = word_counts(str_split(B))
print cosine_sim(d1, d2)
