class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new = newInterval
        res = []
        for index,interval in enumerate(intervals):
            if new[1] < interval[0]:
                return res + [new] + intervals[index:]
            elif not (new[1] < interval[0] or new[0] > interval[1]):
                new = [min(new[0],interval[0]),max(new[1],interval[1])]
            else:
                res.append(interval)
        if not res or (res and res[-1][1] < new[0]):
            res.append(new)
        return res