class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        l, r = 0, len(intervals)-1
        while l <= r:
            mid = (l+r)//2
            if newInterval[0] > intervals[mid][0]:
                l = mid + 1
            else:
                r = mid - 1

        intervals.insert(l, newInterval)
              
        output = [intervals[0]]
        
        for start,end in intervals[1:]:
            if output[-1][1] >= start:
                output[-1][1] = max(output[-1][1], end)
            else:
                output.append([start,end])
        return output