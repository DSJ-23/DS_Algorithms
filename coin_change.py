class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = 0
        coins.sort()
        return self.recur(coins, amount, count)
    
    def recur(self, coins, amount, count):
        
        if amount == 0:
            return count
        
        if max(coins) > amount:
            coins.remove(max(coins))
            return self.recur(coins, amount, count)
        
        if amount > 0:
            amount = amount - max(coins)
            return self.recur(coins, amount, count + 1)
        return -1