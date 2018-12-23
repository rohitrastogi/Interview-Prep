'''
Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].

Input: words = ["timber", "berserk"]
reference string: timber#berserk#

input: words = ["fat", "her", "father"]
reference string: ["father#her#]

input: words = ["time", "father", "her", "ber", "me"]
Note:

1 <= words.length <= 2000.
1 <= words[i].length <= 7.
Each word has only lowercase letters.
'''

def shortest_encoding(words):
    res = 0
    #time complexity: O(n) because word length is constant size 
    for i in range(len(words)):
        words[i] = words[i][::-1]
    #time complexity: O(nlogn)
    words = sorted(words)
    prefix = words[0]
    #time complexity: O(n)
    for i in range(1, len(words)):
        if words[i][:len(prefix)] != prefix:
            prefix = words[i]
            res += len(words[i-1]) + 1
    res += len(words[-1]) + 1
    return res

print(shortest_encoding(['time', 'me', 'e']))

