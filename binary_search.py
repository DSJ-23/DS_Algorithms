a = list(range(1001))


def binary_search(nums, num):
    lower = 0
    upper = len(nums) - 1
    mid = 0
    while lower <= upper:
        
        mid = (lower + upper)//2
        # print(nums[mid])
        if nums[mid] > num:
            upper = mid -1
        elif nums[mid] < num:
            lower = mid + 1
        else:
            return mid
        
    return -1

# for i in range(1001):
#     if binary_search(a, i) != i:
#         print('oh no')
#     else:
#         print('yes')

