import math


def std_of_lengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) < 1:
        return float('NaN')

    vector = [len(i) for i in L]
    mean = sum(vector)/len(vector)
    std = math.sqrt(sum([(x - mean)**2 for x in vector])/len(vector))
    return std

L = ['apples', 'oranges', 'kiwis', 'pineapples']
# L = ['a', 'z', 'p']
print(std_of_lengths(L))
