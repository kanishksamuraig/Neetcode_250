class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new = newInterval
        res = []
        for index,interval in enumerate(intervals):
            if new[1] < interval[0]:
                return res + [new] + intervals[index:]     #append res and return the rest of intervals
            elif not (new[1] < interval[0] or new[0] > interval[1]):
                new = [min(new[0],interval[0]),max(new[1],interval[1])]            #perform merge
            else:
                res.append(interval)                    #append the current interval in the array
        res.append(new)                            #if result array is empty or the last element of the res array has end time less than the start of new interval, append   
        return res