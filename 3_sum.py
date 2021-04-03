# [-4, -1, -1, 0, 1, 2]

nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    if nums == [] or len(nums) == 1:
        return []
    nums.sort()
    result = []
    rr = len(nums)-1
    
    for index, value in enumerate(nums):
        left = index + 1
        right = rr

        if left == right:
            break
        
        cur = nums[left] + nums[right]
        target = value*-1
        while left < right:
            if cur > target:
                right -= 1
            elif cur < target:
                left += 1
            else:
                add = [value, nums[left], nums[right]]
                if add not in result:
                    result.append(add)
                left += 1
            cur = nums[left] + nums[right]
    
    return result


print(threeSum(nums))


class Solution:
    def threeSum(self, nums):
        if nums == [] or len(nums) == 1:
            return []
        nums.sort()
        result = []
        left = 0
        right = len(nums)-2
        for index, value in enumerate(nums):
            skipped = self.skip_number(nums, index)
            make_zero = value*-1
            while left < right:
                
                if skipped[left] + skipped[right] > make_zero:
                    right -= 1
                elif skipped[left] + skipped[right] < make_zero:
                    left +=1 
                elif skipped[left] + skipped[right] == make_zero:
                    to_add = [value, skipped[left],skipped[right]]
                    to_add.sort()
                    if to_add not in result:
                        result.append(to_add)
                    left += 1
            left = 0
            rigt = len(nums)-2
        return result
    
    @staticmethod
    def skip_number(num_array, num_index):
        first = num_array[0:num_index]
        second = num_array[num_index + 1:]
        return first + second



# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if nums == [] or nums == [0]:
#             return []
#         result = []
#         nums.sort()
#         for index, value in enumerate(nums):
#             target = value*-1
#             numbers = self.skip_number(nums, index)
#             temp_result = self.twoSum(numbers, target, value)
#             if (temp_result is not None):
#                 temp_result.sort()
#                 if temp_result not in result:
#                     result.append(temp_result)
#         return (result)
    
#     @staticmethod
#     def twoSum(nums, target, original):
#         seen = {}
#         for index, value in enumerate(nums):
#             lookup = target - value
#             if lookup in seen:
#                 return [value, lookup, original]
#             else:
#                 seen[value] = True
#         return None
    
#     @staticmethod
#     def skip_number(num_array, num_index):
#         first = num_array[0:num_index]
#         second = num_array[num_index + 1:]
#         return first + second


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         if nums == [] or nums == [0]:
#             return []
#         result = []
#         for index, value in enumerate(nums):
#             cached = {}
#             target = value*-1
#             numbers = self.skip_number(nums, index)
#             temp_result = self.twoSum(numbers, target)
#             if (temp_result is not None):
#                 temp_result.append(value)
#                 temp_result.sort()
#                 if temp_result not in result:
#                     result.append(temp_result)
#         return (result)
    
#     @staticmethod
#     def twoSum(nums, target):
#         seen = {}
        
#         for index, value in enumerate(nums):
#             lookup = target - value
#             if lookup in seen:
#                 return [value, lookup]
#             else:
#                 seen[value] = True
#         return None
            
            
#     @staticmethod
#     def skip_number(num_array, num_index):
#         first = num_array[0:num_index]
#         second = num_array[num_index + 1:]
#         return first + second
            



def twoSum(nums, target):
    seen = {}
    
    for index, value in enumerate(nums):
        lookup = target - value
        if lookup in seen:
            return [value, lookup]
        else:
            seen[value] = True
    return None



def skip_number(num_array, num_index):
    first = num_array[0:num_index]
    second = num_array[num_index + 1:]
    return first + second



