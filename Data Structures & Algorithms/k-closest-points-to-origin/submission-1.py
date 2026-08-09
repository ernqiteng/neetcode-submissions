import math, heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap, output = [], []

        for x,y in points:
            heapq.heappush(heap, (math.sqrt(x**2 + y**2), x, y))
        
        for num in range(k):
            length, x, y = heapq.heappop(heap)
            output.append([x,y])
        
        return output