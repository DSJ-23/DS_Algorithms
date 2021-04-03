nums = list(range(1,1001))


def search(nums, target):

    lower = 0
    upper = len(nums)-1
    mid = 0

    while lower <= upper:
        mid = (upper + lower) //2
        print(nums[mid])
        if nums[mid] > target:
            upper = mid + 1
        elif target > nums[mid]:
            lower = mid -1
        else:
            return mid
    return -1


print(search(nums, 333))