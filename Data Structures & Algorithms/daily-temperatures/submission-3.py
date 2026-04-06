class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures);stack=[]
        for index,temp in enumerate(temperatures):
            while stack and stack[-1][0]<temp:
                restemp,resindex=stack.pop()
                res[resindex]=index-resindex
            stack.append((temp,index))
        return res