class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0]
        prev_min = nums[0]
        ans = nums[0]
        
        for i in range(1, len(nums)):
            val = nums[i]
            curr_max = max(prev_max*val, val, prev_min*val)
            curr_min = min(prev_min*val, val, prev_max*val)
            prev_max = curr_max
            prev_min = curr_min
            ans = max(ans, curr_max)
        return ans

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if (len(nums) == 2):
            return max(nums[0], nums[1], nums[0]*nums[1])
        all_filled = list(map(self.conv, nums))
        all_filled[0] = nums[0]
        
        result = 0
        for i in range(1,len(nums)):
            # all_filled[i] = max(nums[i], nums[i]*all_filled[i-1], nums[i]*all_filled[i-1]*all_filled[i-2])
            all_filled[i] = max(abs(nums[i]), abs(nums[i]*all_filled[i-1]))
            if all_filled[i] > result:
                result = all_filled[i]
                
        print(all_filled) 
        return result
        
    def conv(self, x):
        return 0


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_p = nums[0]
        current_p = nums[0]
        for value in nums[1:]:
            current_p = max(current_p*value, value)
            max_p = max(current_p, max_p)
        return max_p


