class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return(len(nums))
        
        
        dp = [0]*len(nums)
        dp[0] = 1
        maxans = 1
        
        for i in range(1, len(dp)):
            maxval = 0
            for j in range(0, i + 1):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])
                j += 1
                
            dp[i] = maxval + 1
            maxans = max(maxans, dp[i])
            i +=1
                 
        
        return(max(dp))
        



class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return(len(nums))
        
        j = 0
        i = 1
        
        dp = [1]*len(nums)
        
        while (j < len(nums)-1):
            print(i)
            if i == j:
                j = 0
                i += 1
            elif nums[i] < nums[j]:
                j += 1
            elif nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] +1)
                j = 0
                i += 1
                 
        print(dp)
        
        return(max(dp))