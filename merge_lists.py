#external sort-like algorithm merge k sorted linked-lists
from queue import PriorityQueue

class ListNode:
    def __init__(self, x, node):
        self.val = x
        self.next = node

#linkedlist implementation
def merge_lists(lists):
    head = None
    pq = PriorityQueue()
    for l in lists:
        pq.put( (l.val, l) )
    while not pq.empty():
        val, node = pq.get()
        if not head:
            head = node
            curr = head
        else:
            curr.next = node
            curr = curr.next
        node = node.next
        if node:
            pq.put( (node.val, node) )
    return head 

def merge_arrays(arrays):
    res = []
    pq = PriorityQueue()
    progress = {k:0 for k in range(len(arrays))}
    for i in range(len(arrays)):

        pq.put( (arrays[i][progress[i]], i) )
    while not pq.empty():
        val, index = pq.get()
        res.append(val)
        progress[index] += 1
        if progress[index] < len(arrays[index]):
            pq.put( (arrays[index][progress[index]], index) )
    return res


def intersection_2_arrays(a1, a2):
    if len(a1) < len(a2):
        array1 = a1
        array2 = a2
    else:
        array1 = a2
        array2 = a1
    res = []
    counts = {}
    for elem in array1:
        if counts[elem]:
            counts[elem] += 1
        else:
            counts[elem] == 1
    for elem in array2:
        if counts[elem]:
            res.append(elem)
            counts[elem] -= 1
    return res 

#if both lists cant fit in memory, you can not use hashmap
#if one can, use that as the hashmap and chunk second list 
#if neither can, use external sort (merge k sorted arrays), then chunk (assuming res can fit into memory)
def intersection_2_sorted_arrays(array1, array2):
    i = 0
    j = 0
    res = []
    while i<len(array1) and j<len(array2):
        print(i, j)
        if array1[i] == array2[j]:
            res.append(array1[i])
            i += 1
            j += 1
        elif array1[i] < array2[j]:
            i += 1
        else:
            j += 1
    return res

print(intersection_2_sorted_arrays([1, 2, 2, 3], [1, 2, 2]))

'''intersection of n sets:
1) sort 
2) map of small
3) binary search on all other sets over map
4) if freq less, update freq
5) if found in all, add char freq times
6) if not found in all sets ignore
'''


# test_arrays = [
#     [1, 2, 3],
#     [1, 2, 2, 5],
#     [3, 3, 4, 5]
# ]
# print(merge_arrays(test_arrays))



