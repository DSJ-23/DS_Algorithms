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



[2,3,-2,-4]
[-3,-1,-1]
[-2,-3,-2,-4]