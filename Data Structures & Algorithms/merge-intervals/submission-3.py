class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x:x[0])
        curr = intervals[0]
        
        for interval in intervals:
            if curr[1] < interval[0]:
                res.append(curr)
                curr = interval
            elif not (curr[1]<interval[0]):
                curr = [min(curr[0],interval[0]),max(curr[1],interval[1])]
        res.append(curr)
        return res