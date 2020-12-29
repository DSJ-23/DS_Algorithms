class Solution:
    def coinChange(self, coins, amount):
        
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        
        for money in range(1, amount+1):
            if money in coins:
                dp[money] = 1
            else:
                minvalue = float('inf')
                for coin in coins:
                    if money-coin > 0:
                        minvalue = min(minvalue, dp[money-coin]+1)
                dp[money] = minvalue

        return dp[amount] if dp[amount] != float('inf') else -1


a = Solution()
print(a.coinChange([3,7,405, 436], 8839))