class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maxwotta=0
        while(r!=l):
            ht=min(heights[r],heights[l])
            area=ht*(r-l)
            maxwotta=max(area,maxwotta)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return maxwotta
            