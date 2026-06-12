class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = [-1 for i in range(len(cost))]
        if len(cost) >= 1:
            mincost[0] = cost[0]
        if len(cost) >= 2:
            mincost[1] = cost[1]
        if len(cost) > 2:
            for i in range(2, len(cost)):
                mincost[i] = cost[i] + min(mincost[i-1], mincost[i-2])
        return min(mincost[-1], mincost[-2])