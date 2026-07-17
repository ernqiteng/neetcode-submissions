class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        numofcoins = {i: float('inf') for i in range(amount+1)}
        numofcoins[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i - coin >= 0:
                    numofcoins[i] = min(numofcoins[i-coin]+1, numofcoins[i])
        return numofcoins[amount] if numofcoins[amount] != float('inf') else -1