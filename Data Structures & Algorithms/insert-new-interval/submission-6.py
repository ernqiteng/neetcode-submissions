class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        overlap = False
        found = False
        i = 0
        newintervals = []
        while not overlap and i < len(intervals):
            if intervals[i][1] < newInterval[0]:
                newintervals.append(intervals[i])
                i+=1
            else:
                overlap = True
        if i == len(intervals):
            newintervals.append(newInterval)
            return newintervals
        if newInterval[1] < intervals[i][0]:
            newintervals.append(newInterval)
        else:
            start = min(intervals[i][0], newInterval[0])
            while not found and i < len(intervals)-1:
                if intervals[i+1][0] <= newInterval[1]:
                    i+=1
                else:
                    found = True
            end = max(intervals[i][1], newInterval[1])
            newintervals.append([start, end])
            i+=1
        while i < len(intervals):
            newintervals.append(intervals[i])
            i+=1
        return newintervals