"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        """
        split intervals into start and end times
        sort
        start time pointer and end time pointer
        while start time pointer has not reached end of list
        process whichever(start/end time pointer) is lower
        count - keeping track of the current simultaneous meetings occuring
        if start time, count += 1
        maxcount = max(maxcount, count)
        else count -= 1
        return maxcount
        """

        startTimes = []
        endTimes = []
        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)
        
        startTimes.sort()
        endTimes.sort()

        startpointer = 0
        endpointer = 0
        count = 0
        maxcount = 0

        while startpointer < len(startTimes):
            if startTimes[startpointer] < endTimes[endpointer]:
                count += 1
                maxcount = max(maxcount, count)
                startpointer += 1
            else:
                count -= 1
                endpointer += 1
        return maxcount
