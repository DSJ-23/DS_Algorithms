class Solution:
    def findDuplicates(self, nums):
        for i in range(1, len(nums) +1):
            if i in nums and nums.count(i) == 1:
                nums.remove(i)
            elif i in nums and nums.count(i) > 1:
                self.remove_nums(nums, i)
            else:
                continue
        return nums

    def remove_nums(self, list_nums, number):
        while list_nums.count(number) != 1:
            list_nums.remove(number)
        return list_nums

eg = [4,3,2,7,8,2,3,1]

a = Solution()

print(a.findDuplicates(eg))