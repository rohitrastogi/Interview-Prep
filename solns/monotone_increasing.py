'''
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9

Example 2:
Input: N = 1234
Output: 1234

Example 3:
Input: N = 332
Output: 299

Input: N = 232
Output: 229

Input: N = 2352
Output: N = 2349

Input: N = 326
Note: N is an integer in the range [0, 10^9].

'''

def largest_monotone_less_than(num):
    if num < 10:
        return num 

    num_str = list(str(num))

    for i in range(len(num_str) - 1, 0, -1):
        if num_str[i] < num_str[i-1]:
            num_str[i] = '9'
            num_str[i-1] = str(int(num_str[i-1]) - 1)
    
    return int(''.join(num_str))

test1 = 1234
test2 = 10 
test3 = 5
test4 = 232
test5 = 2352

print(largest_monotone_less_than(test1))
print(largest_monotone_less_than(test2))
print(largest_monotone_less_than(test3))
print(largest_monotone_less_than(test4))
print(largest_monotone_less_than(test5))
