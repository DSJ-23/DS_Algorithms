class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 1 and n == 1:
            return 1
        
        dp = self.generate_arrays(m,n)
        for M in range(1,m):
            for N in range(1,n):
                dp[M][N] = dp[M-1][N] + dp[M][N-1]   
        return dp[-1][-1]
        
        # generate 2-d array
    def generate_arrays(self,m, n):
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
        return result