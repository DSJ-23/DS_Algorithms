from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        shift = search_rotated(nums)
    
        print(nums[shift])
        if (target >= nums[0]):
            print(nums[0:shift])
            return binary_search(nums[0:shift], target)
        result = binary_search(nums[shift:], target) + shift
        return result
        

def search_rotated(nums):
    low = 0
    up = len(nums) -1
    mid = 0

    while low < up:
        mid = (low + up)//2
        a = nums[mid]

        if a > nums[-1]:
            low = mid + 1
        else:
            up = mid
            
    return mid

def binary_search(nums, num):
    lower = 0
    upper = len(nums) - 1
    mid = 0
    while lower <= upper:
        
        mid = (lower + upper)//2
        if nums[mid] > num:
            upper = mid -1
        elif nums[mid] < num:
            lower = mid + 1
        else:
            return mid
        
    return -1
    



# def search(self, nums: List[int], target: int) -> int:
        
#         low = 0
#         up = len(nums) -1
#         mid = 0
        
#         while nums[mid] < nums[mid+1]:
#             mid = (low + up)//2
        
#         return mid

def search(nums, target):

    if len(nums)==1:
        if nums[0]==target:
            return 0
        return -1
    
    last = len(nums)-1
    last_value = nums[last]
    
    while nums[last] <= last_value:
        if last == 0:
            break
        last = int(last/2)
        
    while nums[last] > nums[last-1]:
        last += 1
        
    
    if nums[last]==target:
        return last
    
    return -1

nums = [1,2]
# print(search(nums, 1))


a = [5,6,7,8,9,0,1,2,3,4]
b = [10,11,12,13] + list(range(0,10))
c = [3,4,5,6,7,8]+ [0,1,2]
d = [3,4] + [1,2]
e = list(range(3,17)) + [0,1,2]
# print(b)

def search_rotated(nums):
        print(nums)
        low = 0
        up = len(nums) -1
        mid = 0

        while low < up:
            mid = (low + up)//2
            a = nums[mid]

            if a > nums[-1]:
                low = mid + 1
            else:
                up = mid
            
        return nums[mid]

print(search_rotated(e))