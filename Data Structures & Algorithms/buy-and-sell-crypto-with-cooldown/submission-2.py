class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = {} #key = index, owns   value = maxprofit
        def backtrack(index, owns):
            nonlocal maxprofit
            if index >= len(prices):
                return 0
            
            if (index, owns) in maxprofit:
                return maxprofit[(index, owns)]
            
            #don't buy/sell
            leave = backtrack(index+1, owns)
            if not owns:
                #buy
                maxprofit[(index, owns)] = max(backtrack(index+1, True)-prices[index], leave)
            else:
                #sell 
                maxprofit[(index, owns)] = max(backtrack(index+2, False)+prices[index], leave)
            return maxprofit[(index, owns)]

        return backtrack(0,False)