# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        line = [root1, root2]
        result = []
        while line != []:
            current = line.pop(0)
            if current.left:
                line.append(current.left)
            if current.right:
                line.append(current.right)
        return result
    
    def asc_root(self, root):