class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
       
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        if len(nums) == 2:
            return dp[1]
       
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[-1]




class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if (len(nums) == 2):
            return max(nums[0], nums[1])
        all_filled = list(map(self.conv, nums))
        all_filled[0] = nums[0]
        for i in range(0, len(nums)):
            all_filled[i] = max((all_filled[i-2]+nums[i]), (all_filled[i-1]))
        return all_filled[-1]
    
    def conv(self, x):
        return 0