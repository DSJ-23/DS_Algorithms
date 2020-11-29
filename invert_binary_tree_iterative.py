class Solution:
    def invertTree(self, root):
        if root is None:
            return root
        
        line = [root]
        while line != []:
            to_change = line.pop(0)
            left = to_change.left
            right = to_change.right
            
            if left is not None:
                line.append(left)
            if right is not None:
                line.append(right)
                    
            to_change.left = right
            to_change.right = left
        return root