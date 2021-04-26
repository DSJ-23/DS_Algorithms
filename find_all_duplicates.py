# Runtime: 340 ms, faster than 85.15% of Python3 online submissions for Find All Duplicates in an Array.
# Memory Usage: 23.4 MB, less than 13.19% of Python3 online submissions for Find All Duplicates in an Array.

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []
        for i in nums:
            if i in seen:
                result.append(i)
            seen.add(i)
        return result


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
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
        