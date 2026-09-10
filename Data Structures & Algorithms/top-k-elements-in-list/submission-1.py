import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        iterate over nums list
        dict
        key - number, value - number of times it appears
        use
        max heap
        pop from heap k times
        """
        numbers = {}
        for num in nums:
            numbers[num] = numbers.get(num, 0) + 1
        
        heap = []
        for num in numbers.keys():
            heapq.heappush(heap, [-numbers[num],num])

        output = []
        for i in range(k):
            occurrences, num = heapq.heappop(heap)
            output.append(num)
        return output
