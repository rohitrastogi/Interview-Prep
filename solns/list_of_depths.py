from collections import deque 

class Tree():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class TreeLink():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None

class LL():
    def __init__(self, val):
        self.val = val
        self.next = None

#input is of type Tree
def lod(node):
    res = []
    queue = deque([(node, 0)])
    curr = None
    while queue:
        node, depth = queue.popleft()
        new_ll = LL(node.val)
        if len(res) < depth + 1:
            res.append(new_ll)
            curr = new_ll
        else:
            curr.next = new_ll
            curr = curr.next
        if node.left:
            queue.append([(node.left, depth + 1)])
        if node.right:
            queue.append([(node.right, depth + 1)])
    return res 

#leetcode 116
#input is of type tree Link
# O(n) space and time
def connect_it(node):
    queue = deque([(node, 1)])
    curr = None
    curr_depth = 0
    while queue:
        node, depth = queue.popleft()
        if depth > curr_depth:
            curr = node
            curr_depth += 1
        else:
            curr.next = node
            curr = curr.next
            if node.left:
                queue.append([(node.left, depth + 1)])
            if node.right:
                queue.append([(node.right, depth + 1)])

# O(n) time and O(1) space
def connect_rec(node):
    if not node:
        return
    #connect left child
    if node.left:
        node.left.next = node.right
    #connect right child
    if node.next and node.right:
        node.right.next = node.next.left
    connect_rec(node.left)
    connect_rec(node.right)






        