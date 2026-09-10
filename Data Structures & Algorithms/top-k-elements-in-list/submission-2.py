import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for num in nums:
            numbers[num] = numbers.get(num, 0) + 1
        
        heap = []
        for num in numbers.keys():
            heapq.heappush(heap, [numbers[num],num])

            if len(heap) > k:
                heapq.heappop(heap)

        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        return output
