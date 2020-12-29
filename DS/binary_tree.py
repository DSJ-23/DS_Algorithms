class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a = TreeNode(val=5)
a.left = TreeNode(val=3)
a.right = TreeNode(val=8)

a.left.left = TreeNode(val = 1)
a.left.right = TreeNode(val=4)

a.right.right = TreeNode(val=9)
a.right.left = TreeNode(val=7)

print(a.__dict__)
