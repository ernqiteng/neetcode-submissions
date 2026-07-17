class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        graph
        broken down in diff ways
        """
        if amount == 0: return 0
        numofcoins = {i:float('inf') for i in range(amount+1)}
        for coin in coins:
            numofcoins[coin] = 1
        for i in range(amount+1):
            for coin in coins:
                if i - coin > 0:
                    numofcoins[i] = min(numofcoins[i-coin]+1, numofcoins[i])
        return numofcoins[amount] if numofcoins[amount] != float('inf') else -1