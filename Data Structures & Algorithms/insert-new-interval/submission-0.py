class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        new = newInterval
        for inter in intervals:
            if new:
                if (inter[0]<=new[1] and inter[0]>=new[0]) or (inter[1]>=new[0] and inter[1]<=new[1]) or (inter[0]>=new[0] and inter[1]<=new[1]) or (inter[0]<=new[0] and inter[1]>=new[1]):
                    new = [min(inter[0],new[0]),max(inter[1],new[1])]
                    continue
                elif inter[0] > new[1]:
                    stack.append(new)
                    new = None
            
            stack.append(inter)
        if new:
            stack.append(new)
            new = None
        return stack