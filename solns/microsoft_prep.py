def mergesort(l):
    if len(l) > 1:
        mid = len(l)//2
        sub1 = mergesort(l[:mid])
        sub2 = mergesort(l[mid:])
        return merge(sub1, sub2)
    else:
        return l

def merge(l1, l2):
    merged = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            merged.append(l1[i])
            i+= 1
        else:
            merged.append(l2[j])
            j+=1

    while i < len(l1):
        merged.append(l1[i])
        i+= 1

    while j < len(l2):
        merged.append(l2[j])
        j+=1
    
    return merged

#Cases:
'''
Empty List -> Empty List
Length of size 1 -> Return list
Length of size > 1 -> Return sorted
'''

def binary_search(l, val):
    left = 0
    right = len(l) - 1
    while left <= right:
        mid = (left + right)//2
        if val > mid:
            left = mid + 1
        elif val < mid:
            right = mid - 1
        else:
            return True
    return False

class Node():
    def __init__(self, val):
        self.val = val  
        self.next = None

class LL():
    def __init__(self):
        self.root = None

    '''
    Case 1: Empty List -> Exception
    Case 2: Delete from head
    Case 3: Delete from middle or end
    1 2 3 4 
    '''

    def delete(self, val):
        if not self.root:
            raise Exception("Cannot Delete from Empty List")
        if self.root.val == val:
            self.root = self.root.next
            return
        curr = self.root
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                return
            curr = curr.next

    def delete_ith(self, i):
        if not self.root:
            raise Exception("Cannot delete element from empty list!")

        count = 0
        if count == i:
            self.root = self.root.next
            return 
        
        curr = self.root
        while curr.next:
            if count + 1 == i:
                curr.next = curr.next.next
                return 
            curr = curr.next
            count += 1
        
        raise Exception("List does not include ith element!")

    def print_ll(self):
        curr = self.root
        while curr:
            print(curr.val)
            curr = curr.next

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lowest_common_ancestor_BST(root, node1, node2):
    if node1 > node2:
        node1, node2 = node2, node1
    
    if root < node1 and root < node2:
        return lowest_common_ancestor_BST(root.left, node1, node2)

    if root > node1 and root > node2:
        return lowest_common_ancestor_BST(root.right, node1, node1)

    return root

'''
logic:
- (None, False) if neither node1 or node2 are found in the subtree
- (Val, True) Val is the lowest common ancestor 
- (Val, False) Val is either node1 or node2 but is not the LCA
'''
def LCA_helper(root, node1, node2):
    if not root:
        return (None, False)
    if root.val == node1 and root.val == node2:
        return (root.val, True)

    left = LCA_helper(root.left, node1, node2)
    if left[1]:
        return left

    right = LCA_helper(root.right, node1, node2)
    if right[1]:
        return right

    if left[0] and right[0]:
        return (root.val, True)
    
    if root.val == node1 or root.val == node2:
        isAncestor = left[0] or right[0]
        return (root.val, isAncestor)

    else:
        if left[0] or right[0]:
            found = left[0] if left[0] is not None else right[0]
            return (found, False )
        if not left[0] and not right[0]:
            return (None, False)

def LCA(root, node1, node2):
    res = LCA_helper(root, node1, node2)
    if res[1]:
        return res[0]
    raise Exception("Node1 and Node2 are not both in the provided tree.")

def successor(node):
    pass

def reverse_number(num):
    remaining = num
    rev = 0
    while remaining > 0:
        new_digit = remaining % 10
        rev = new_digit + rev * 10
        remaining = remaining // 10
    return rev 

def detect_ll_cycle(root):
    pass

def reverse_sentence(sentence):
    res = []
    split = sentence.split(' ')
    for i in range(len(split) -1, -1, -1):
        res.append(split[i])
    return ' '.join(res)
    # return ' '.join(split[::-1])

def generate_subsets(s):
    res = []

    def generate_subsets_helper(curr_subset, index):
        if index == len(s):
            res.append(curr_subset)
            return

        generate_subsets_helper(curr_subset, index + 1)
        generate_subsets_helper(curr_subset + [s[index]], index + 1)
    
    generate_subsets_helper([], 0)
    print(len(res))
    return res
    

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(12)

# print(LCA(root, 2, 9))

# print(reverse_sentence('I kicked the ball very far'))
# print(generate_subsets([1,2,3,4]))
print(reverse_number(12345))
