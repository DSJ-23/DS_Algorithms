nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6,8]

m = 3
n = 3

#do not create a new array, modify nums1 in place and return it
def merge(nums1, m, nums2, n):
    first_index = 0
    second_index = 0
        
    insert = m + 1


lenght_2 = (len(nums2) // 2)
print(nums2[lenght_2])


 
        if nums1[0] != 0:
            while nums1[-1] == 0:
                nums1.pop()
            nums1 = self.merge_iterative(nums1, nums2)
        else:
            for index, value in enumerate(nums1):
                if value 

def merge_iterative(self,num1, num2):
        first = 0

        if num1 is None:
            return num2
        if num2 is None:
            return num1

        while len(num2) > 0:
            if first == len(num1):
                for i in num2:
                    num1.insert(first, i)
                    first += first
                break
            elif num2[0] > num1[first]:
                first = first + 1
            elif num2[0] <= num1[first]:
                num1.insert(first, num2.pop(0))
        return num1

while len(nums2) > 0:
            # print(nums1)
            # print(in_first)
            # print(last)
            if nums2[-1] >= nums1[in_first]:
                to_add = nums2.pop()
                nums1[last] = to_add
            else:
                nums1[last] = nums1[in_first]
                in_first = in_first -1
            
            last = last -1

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        in_first = m -1
        last = len(nums1) - 1
        second = n -1
        
        while second >= 0:
            if in_first < 0:
                pass
            elif second < d
            if nums2[second] >= nums1[in_first]:
                nums1[last] = nums2[second]
                second = second -1 
            else:
                nums1[last] = nums1[in_first]
                in_first = in_first -1
            last = last -1
                

                    

