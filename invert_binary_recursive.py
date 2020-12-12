class Solution:
    def invertTree(self, root):
        self.divide_conquer(root)
        if root:
            return root
        else:
            return None
        
    def divide_conquer(self, node):
        if node:
            left = node.left
            node.left = node.right
            node.right = left
            if node.left:
                self.divide_conquer(node.left)
            if node.right:
                self.divide_conquer(node.right)