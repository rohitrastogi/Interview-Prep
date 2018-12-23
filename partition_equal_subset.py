'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''

#idea 1: recursively generate all partitions

def equal_sum_partition(arr):
    def helper(s1, s2, i):
        print(s1, s2, i)
        if i == len(arr):
            if not s1 or not s2:
                return False
            if sum(s1) == sum(s2):
                return True
        else:
            return helper(s1 + [arr[i]], s2, i + 1) or helper(s1, s2 + [arr[i]], i + 1)
    return helper([], [], 0)

test1 = [1, 2, 3, 5]
test2 = [1, 5, 11, 5]
print(equal_sum_partition(test1))
print(equal_sum_partition(test2))


#idea 2 - divide by 2 and run subset sum (duh)