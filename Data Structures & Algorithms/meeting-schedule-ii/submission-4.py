"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()
        s = e = 0
        count = 0
        maxcount = 0
        while s<len(start) and e<len(end):
            if start[s] < end[e]:
                count+=1
                s+=1
            else:
                count -=1
                e+=1
            maxcount = max(count,maxcount)
        return maxcount
