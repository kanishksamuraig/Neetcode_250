class Solution:
    def trap(self, height: List[int]) -> int:
        #brute force 
        area = 0
        for i in range(len(height)):
            left=i-1; right = i+1;maxleft=maxright=-1
            while left>=0:
                maxleft = max(maxleft,height[left])
                left-=1
            while right<len(height):
                maxright = max(maxright,height[right])
                right+=1
            if min(maxleft,maxright) > height[i]:
                area += min(maxleft, maxright) - height[i]
        return area