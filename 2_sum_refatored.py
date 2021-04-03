nums= [2,7,11,15]

def twoSum(nums, target): 
        left = 0
        right = len(nums)-1
        
        cur = nums[left] + nums[right]
        
        while cur != target:
            if cur > target:
                right -= 1
            else:
                left += 1
            cur = nums[left] + nums[right]
        return [left, right]

print(twoSum(nums, 9))