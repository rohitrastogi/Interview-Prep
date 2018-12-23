'''
other problems:
- immutable tree
- binary tree - common ancestor between two nodes
- heapify 
'''

class TreeNode():
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
        self.count = 0

def insert_naive(curr_node, new_val):
    if not curr_node.val:
        curr_node.val = new_val
    elif new_val > curr_node.val:
        if curr_node.right:
            insert_naive(curr_node.right, new_val)
        else:
            curr_node.right = TreeNode(new_val)
    elif new_val < curr_node.val:
        if curr_node.left:
            insert_naive(curr_node.left, new_val)
        else:
            curr_node.left = TreeNode(new_val)
    else:
        curr_node.val.count += 1

def contains(curr_node, key):
    if not curr_node:
        return False 
    if key < curr_node.val:
        return contains(curr_node.left, key)
    elif key > curr_node.val:
        return contains(curr_node.right, key)
    else:
        return True

def get_height(curr_node):
    if not curr_node:
        return 0
    return 1 + max(get_height(curr_node.left), get_height(curr_node.right))

# simple left/right check is not sufficient
def validate_helper(curr_node, lower, upper):
    if not curr_node:
        return True
    else:
        if curr_node.val > lower and curr_node.val < upper:
            return validate_helper(curr_node.left, lower , curr_node.val) and validate_helper(curr_node.right, curr_node.val, upper)
        return False 

def validate(node):
    return validate_helper(node, float('-inf'), float('inf'))

def insert_avl(node, key):
    pass

def delete_naive(node, key):
    pass 

def delete_avl(node, key):
    pass 

#bubble down and up
def is_balanced_helper(tree):
    if not tree:
        return 0

    left_height = is_balanced_helper(tree.left)
    if left_height == float('-inf'):
        return float('-inf')

    right_height = is_balanced_helper(tree.right)
    if right_height == float('-inf'):
        return float('-inf')

    if abs(right_height - left_height) > 1:
        return float('-inf')
    else:
        return max(left_height, right_height) + 1

def is_balanced(tree):
    return is_balanced_helper(tree) != float('-inf')

def invert(node):
    if not node:
        return
    node.left, node.right = node.right, node.left
    invert(node.left)
    invert(node.right)
    
def is_symmetric(tree):
    return is_symmetric_helper(tree.left, tree.right)

def is_symmetric_helper(left, right):
    if not left and not right:
        return True
    return left.val == right.val and is_symmetric_helper(left.left, right.right) and is_symmetric_helper(left.right, right.left)

def equals(tree, subtree):
    if not tree and not subtree:
        return True
    if not tree or not subtree:
        return False 
    return tree.val == subtree.val and equals(tree.left, subtree.left) and equals(tree.left, subtree.right)

def is_subtree(tree, subtree):
    if not tree:
        return False
    if not subtree:
        return True
    return equals(tree, subtree) or is_subtree(tree.left, subtree) or is_subtree(tree.right, subtree)

def closest_element_helper(key, tree, min_diff, min_diff_key):
    if not tree:
        return min_diff_key
    if key == tree.val:
        return key
    if abs(key - tree.val) < min_diff:
        min_diff = abs(key - tree.val)
        min_diff_key = tree.val
    if key < tree.val:
        return closest_element_helper(key, tree.left, min_diff, min_diff_key )
    return closest_element_helper(key, tree.right, min_diff, min_diff_key)

def closest_element(key, tree):
    return closest_element_helper(key, tree, float('inf'), None)
    
def successor(lol):
    pass

def select_random(tree):
    pass

def rotate_right(lol):
    pass

def left_rotate(lol):
    pass 

test = TreeNode()
insert_naive(test, 7)
insert_naive(test, 3)
insert_naive(test, 9)
print(contains(test, 7))
print(contains(test, 3))
print(contains(test, 9))
print(contains(test, 10))
print(get_height(test))
print(validate(test))
print(closest_element(4, test))
