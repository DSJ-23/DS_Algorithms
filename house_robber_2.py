# Runtime: 32 ms, faster than 63.05% of Python3 online submissions for House Robber II.
# Memory Usage: 14.4 MB, less than 25.38% of Python3 online submissions for House Robber II.


from typing import List

a = [2,3,2]

b = [1]

def rob(nums: List[int]) -> int:

    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]

    first = base(nums[1:])
    second = base(nums[:-1])
    return max(first, second)


def base(nums: List[int]) -> int:
    print(nums)
    if len(nums) == 0:
            return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0]*len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    print(dp)
    return dp[-1]

print(rob(b))

# print(base(a[1:]))
# print(base(a[:-1]))