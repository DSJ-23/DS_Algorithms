class Solution:
    def coinChange(self, coins, amount):
        coins.sort()
        count = 0
        
        while len(coins) > 0:
            pointer = len(coins) - 1
            to_remove = coins[pointer]
            if amount >= to_remove:
                amount = amount - to_remove
                count += 1
            elif to_remove >= amount:
                coins.remove(to_remove)
            print(count, amount)
        if amount == 0:
            return count
        return -1

a = Solution()
print(a.coinChange([3,7,405, 436], 8839))


# print(a.coinChange([2], 3))