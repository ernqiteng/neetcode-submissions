class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newintervals = []
        newintervals.append(intervals[0])
        i = 1
        while i < len(intervals):
            print(newintervals)
            if intervals[i][0] <= newintervals[-1][1]:
                #overlap
                newintervals[-1][1] = max(newintervals[-1][1], intervals[i][1])
            else:
                newintervals.append(intervals[i])
            i += 1
        return newintervals