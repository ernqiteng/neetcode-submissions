"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes, endTimes = [], []
        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)
        
        startTimes.sort()
        endTimes.sort()

        startpointer, endpointer, count, maxcount = 0, 0, 0, 0

        while startpointer < len(startTimes):
            if startTimes[startpointer] < endTimes[endpointer]:
                count += 1
                maxcount = max(maxcount, count)
                startpointer += 1
            else:
                count -= 1
                endpointer += 1
        return maxcount
