from itertools import permutations
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        moves = (m-1)+(n-1)
        perm = permutations(list(range(0,moves)))
        perm = len(list(perm))
        perm = perm/(math.factorial(m-1)*math.factorial(n-1))
        return int(perm)

print(math.factorial(5))

# perm = permutations([1,2,3,4,5])
# print(len(list(perm)))

def print_double(array):
    for i in array:
        print(i)
    return

def generate_arrays(m, n):
    result = []
    for i in range(0,m):
        number_ini = 0
        first = 1
        if result == []:
            number_ini = 1
            first = 0
        l = [number_ini]*n
        l[0] = first
        result.append(l)
    # print_double(result)
    return result

def iterate_2d(m,n):
    dp = generate_arrays(m,n)
    for M in range(1,m):
        for N in range(1,n):
            dp[M][N] = dp[M-1][N] + dp[M][N-1]   
    return dp[-1][-1]


