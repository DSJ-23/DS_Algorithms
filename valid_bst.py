# [5,4,6,null,null,3,7]

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        result = True
        
        if root is None:
            return False
        
        def traverse(root):
            nonlocal result
            if root is None:
                return
            if root.left:
                if root.left.val > root.val:
                    result = False
            if root.right:
                if root.right.val < root.val:
                    result = False
            traverse(root.left)
            traverse(root.right)
            
        traverse(root)
        return result