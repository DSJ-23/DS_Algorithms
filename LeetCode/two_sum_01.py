# class Solution():

#     def twoSum(self, )


# def twoSum(nums, target):
#     for number in nums:
#         looking_for = target - number
#         if looking_for in nums


def twoSum(nums, target):
    for index, number in enumerate(nums):
        looking_for = target - number
        if looking_for in nums and nums.index(looking_for) != index:
            return [index, nums.index(looking_for)]

print(twoSum([3,3],6))

# print(twoSum([10,9,8], 8))
        