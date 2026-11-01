class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new = newInterval
        for i in range(len(intervals)):
            if new[1]<intervals[i][0]:
                res.append(new)
                return res + intervals[i:]
            elif not (intervals[i][0] > new[1] or intervals[i][1] < new[0]):
                new = [min(new[0],intervals[i][0]),max(new[1],intervals[i][1])]
            else:
                res.append(intervals[i])
        res.append(new)
        return res