
a = list(range(100))

def bin_search(nums, num):

    # print(a)

    lower = 0
    upper = len(nums)-1
    mid = 0

    while lower <= upper:
        mid = (lower + upper)//2
        if nums[mid] > num:
            upper = mid - 1
        elif num > nums[mid]:
            lower = mid + 1
        else:
            return mid
    return -1

for i in range(0, 100):
    if i == bin_search(a, i):
        print('yes')
    else:
        print('no')