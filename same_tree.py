
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            return False
        return False


# class Solution:
#     def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
#         a = self.traverse(p)
#         b = self.traverse(q)
#         print(a,b)
#         if a == b:
#             return True
#         return False
        
#     def traverse(self, root):
        
#         values = []
        
#         def inorder(root):
#             if root is None:
#                 values.append(None)
#                 return 
#             inorder(root.left)
#             values.append(root.val)
#             inorder(root.right)
#         inorder(root)
#         return values