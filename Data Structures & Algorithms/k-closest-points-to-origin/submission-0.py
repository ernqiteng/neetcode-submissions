import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        so points [x,y] -- calculate the distane of each points
        then i will put the distanves in a max heap
        min heap.... negating the distances

        k closest.. once len of  maxheap > k: remove the largest

        make my result array to be returned
        """

        max_heap = []
        res = []

        for x,y in points:
            distance = math.sqrt((x**2) + (y**2))
            heapq.heappush(max_heap, (-distance, x, y))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        for d,x,y in max_heap:
            res.append([x,y])
        return res
        