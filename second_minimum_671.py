
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None or root.right is None:
            return -1
        s_min = root.val
        if root.right.val > root.val:
            s_min = root.right.val
        if root.left.val > root.val:
            s_min = root.left.val
        
        line = [root]
        while line != []:
            current = line.pop(0)
            if current.right is not None:
                line.append(current.right)
            if current.left is not None:
                line.append(current.left)
            if current.val < s_min and current.val != root.val:
                s_min = current.val
            
        if s_min != root.val:
            return s_min
        return -1


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None:
            return -1
        
        s_min = root.val
        
        if root.right is None and root.left is None:
            return -1
        
        if root.right.val is not None:
            s_min = root.right.val
        if root.left.val is not None and root.left.val != root.val:
            s_min = root.left.val
        
        line = [root]
        while line != []:
            current = line.pop(0)
            if current.right is not None:
                line.append(current.right)
            if current.left is not None:
                line.append(current.left)
            if current.val > root.val and current.val < s_min:
                s_min = current.val
            
        if s_min != root.val:
            return s_min
        return -1

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None:
            return -1
        
        if root.right is None and root.left is None:
            return -1
        
        s_min = root.val
        
        line = [root]
        while line != []:
            current = line.pop(0)
            if current.right is not None:
                line.append(current.right)
            if current.left is not None:
                line.append(current.left)
            if (current.val > root.val) and current.val != root.val:
                s_min = current.val
                
        print(s_min)
            
        if s_min != root.val:
            return s_min
        return -1


[5,8,5]
[1,1,1,1,5,1,4]
