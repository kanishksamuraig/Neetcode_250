class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        n=-1
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
            if d[i]>len(nums)//2:
                return i 
        
