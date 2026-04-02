class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            max1 = stones.pop()
            max2 = stones.pop()
            if max1 > max2:
                print(max1, max2, max1-max2)
                max1 = max1-max2
                stones.append(max1)
                stones.sort()
        if len(stones) == 1:
            return stones[0]
        else:
            return 0