class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        curr = intervals[0]
        print(intervals)
        for i in range(1,len(intervals)):
            if curr[1] > intervals[i][0]:
                count += 1
                if curr[1] >=intervals[i][1]:
                    curr = intervals[i]
            else:
                curr = intervals[i]
        return count
