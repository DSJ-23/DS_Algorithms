
# Runtime: 36 ms, faster than 89.99% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.8 MB, less than 23.37% of Python3 online submissions for Search in Rotated Sorted Array.


from typing import List
nums = [4,5,6,7,0,1,2]
a = [5,6,7,8,9,0,1,2,3,4]
b = [10,11,12,13] + list(range(0,10))
c = [3,4,5,6,7,8]+ [0,1,2]
d = [3,4] + [1,2]
e = list(range(3,17)) + [0,1,2]
f = list(range(20,57)) + list(range(0,20))
g = list(range(0,6))

def search_rotated(nums):
    low = 0
    up = len(nums) -1
    mid = 0

    while low < up:
        mid = (low + up)//2
        a = nums[mid]
        if a > nums[mid+1]:
            break
        if a > nums[-1]:
            low = mid + 1
        else:
            up = mid
            
    return mid

print(search_rotated(g))

# print(search_rotated(f))
# print("")
# print(nums, target)
# print(f"shift {shift}")
# print(f"lower {lower}")
# print(f"upper {upper}")
# print(f"nums[mid] {nums[shift]}")

def search(nums: List[int], target: int) -> int:
    if len(nums)==0:
        return -1
    shift = search_rotated(nums)
    a = nums[shift]
    lower = 0
    upper=len(nums)-1

    # print(a, target)

    if a == target:
        return shift
    elif target >= nums[0]:
        upper = shift -1
    elif target < nums[0]:
        lower = shift + 1


    while lower <= upper:
        mid = (lower + upper)//2
        temp = nums[mid]
        if temp > target:
            upper = mid -1
        elif temp < target:
            lower = mid + 1
        else:
            return mid
    
    return -1

# nums = [4,5,6,7,0,1,2]
# a = [5,6,7,8,9,0,1,2,3,4]
# b = [10,11,12,13] + list(range(0,10))
# c = [3,4,5,6,7,8]+ [0,1,2]
# d = [3,4] + [1,2]
# e = list(range(3,17)) + [0,1,2]
# f = list(range(20,57)) + list(range(0,20))
        
# print(search(nums, 1)) #4
# print(nums.index(1))

# print(search(a, 0))
# print(search(b, 0))
# print(search(c, 0))
# print(search(d, 0))
# print(search(e, 0))