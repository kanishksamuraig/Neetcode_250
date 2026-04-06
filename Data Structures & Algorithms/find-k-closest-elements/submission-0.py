class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        left=0;right=len(nums)-1;lst=[]
        while right-left>=k:
            if abs(nums[left]-x)<=abs(nums[right]-x):
                right-=1
            else:
                left+=1
            
        lst=[]
        for i in range(left,right+1):
            lst.append(nums[i])
        return lst
