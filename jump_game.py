class Solution:
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        dp = [0]*(len(nums))
        
        for index, value in enumerate(nums):
            if (dp[index]==1) or (index == 0):
                for i in range(1, value+1):
                    try:
                        dp[index+i] = 1
                    except:
                        pass
        
        return dp[-1] == 1