#not great 22/34

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left= [1]*(len(nums))
        right = [1]*(len(nums))
        
        left_mult = 1
        for index, value in enumerate(nums[1:]):
            left_mult= left_mult*nums[index]
            left[index+1] = left_mult
            
        right_mult = 1
        index_right = len(nums) -1
        for ind, val in enumerate(nums[:-1]):
            right_mult = right_mult*nums[index_right]
            right[index_right-1] = right_mult
            index_right -= 1
            
        
        result = []
        for i, va in enumerate(left):
            result.append(left[i]*right[i])
        
        return(result)