class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        line = [root]
        freq = {}
        while line != []:
            a = line.pop(0)
            if a.val in freq:
                freq[a.val] += 1
            else:
                freq[a.val] = 1
            if a.left:
                line.append(a.left)
            if a.right:
                line.append(a.right)
        mode = max(freq, key=freq.get)
        res = [mode]
        for i in freq:
            if freq[i] == mode and i not in res:
                res.append(i)
        return res