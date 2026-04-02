class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                if prices[j] - prices[i] > max:
                    max = prices[j] - prices[i]
        return max