class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=0;r=0;k=len(nums)
        while(l<len(nums) and r<len(nums)):
            if nums[l]==val and nums[r]==val:
                r+=1
            elif nums[l]==val and nums[r]!=val:
                nums[l]=nums[r]
                l+=1
                r+=1
                k-=1
            elif nums[l]!=val and nums[r]==val:
                r+=1
                k-=1
            else:
                nums[l]=nums[r]
                l+=1
                r+=1
        return l
