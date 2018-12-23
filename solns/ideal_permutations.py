#Local Inversions are a subset of Global Inversions so |Local Inversions| <= |Global Versions|

def isIdealPermutation(s):
    for i in range(len(s)):
        if abs(i - s[i]) > 1:
            return False
    return True