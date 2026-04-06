class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        t=len(nums);i=0
        while i<t:
            if nums[i]==val:
                for j in range(i,t-1):
                    nums[j]=nums[j+1]
                t-=1
                continue
            i+=1
        return t