class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

def print_paths(node, path=[]):
    if not node:
        return
    path.append(node.val)

    if not node.left and not node.right:
        print(path)
        
    print_paths(node.left, path)
    print_paths(node.right, path)
    path.pop()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(7)

print_paths(root)