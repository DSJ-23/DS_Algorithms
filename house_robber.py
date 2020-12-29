class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if (len(nums) == 2):
            return max(nums[0], nums[1])
        all_filled = list(map(self.conv, nums))
        all_filled[0] = nums[0]
        all_filled[1] = nums[1]
        for i in range(2, len(nums)):
            all_filled[i] = max((all_filled[i-2]+nums[i]), (all_filled[i-1]))
        return all_filled[-1]
    
    def conv(self, x):
        return float('inf')

a = [1,2,3,4,5]

for i in range(2, len(a)):
    print(a[i])

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if (len(nums) == 2):
            return max(nums[0], nums[1])
        if (len(nums) == 3):
            return max(nums[2]+nums[0], nums[1])
        all_filled = list(map(self.conv, nums))
        all_filled[0] = nums[0]
        all_filled[1] = nums[1]
        all_filled[2] = nums[2]
        for i in range(2, len(nums)):
            if len(all_filled) <= 3:
                all_filled[i] = max((all_filled[i-2]+nums[i]), (all_filled[i-1]))
            else:
                all_filled[i] = max((all_filled[i-2]+nums[i]), (all_filled[i-1]),(all_filled[i-3]+nums[i]) )
        print(all_filled)
        return all_filled[-1]
    
    def conv(self, x):
        return float('inf')

[1,2,3,1,1,100]
