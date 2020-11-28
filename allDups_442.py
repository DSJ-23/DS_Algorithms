class Solution:

    def findDuplicates(self, nums):
        freq = self.count_dict(nums)
        aa = list(filter(lambda x: freq[x] > 1, nums))
        for i in aa:
            aa = self.only_once(aa, i)
        return aa

    def only_once(self, list_number, number):
        while list_number.count(number) > 1:
            list_number.remove(number)
        return list_number

    def count_dict(self,list_number):
        values = dict.fromkeys(list_number)
        for i in list_number:
            values[i] = list_number.count(i)
        return values


eg = [4,3,2,7,8,2,3,1]
print(max(eg))
print(eg[1:])

# a = Solution()
# print(a.findDuplicates(eg))

