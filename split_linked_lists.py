# # 725.py
# #linked list problem
# #leetcode medium
'''
1) get length of ll
2) divide length by k and add  1 if there is a remainder to determine the size of each piece
3) iterate over ll and maintain counter
    if counter mod size of each part is 0, add to list
    if counter - length less than size, decrement size of piece
        if count is 1 - > fill empties 
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, node):
        self.val = x
        self.next = node

    def get_length(self):
        ln = self
        size = 0
        while ln:
            ln = ln.next
            size += 1
        return size 

def splitListToParts(ln, k):
    curr = ln
    prev = None
    res = []
    length = ln.get_length()
    part_size = length//k
    remainder = length%k == 0 
    #loop over number of parts
    for part_num in range(k):
        if prev:
               prev.next = None
        new_node = curr
        res.append(new_node)
        for elem_num in range(part_size + (part_num < remainder)):
            prev = curr
            curr = curr.next
    return res


    
test1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
print(test1.get_length())
# print(splitListToParts(test1, 2))
