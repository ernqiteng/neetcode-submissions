class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newintervals = []
        newintervals.append(intervals[0])
        for i in range(1, len(intervals)):
            if newintervals[-1][1] >= intervals[i][0]:
                newintervals[-1] = [min(newintervals[-1][0], intervals[i][0]), max(newintervals[-1][1], intervals[i][1])]
            else:
                newintervals.append(intervals[i])
        return newintervals