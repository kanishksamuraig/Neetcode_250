class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max=0
        for i in range(len(nums)):
            if nums[i]>max:
                max=nums[i]
            
        for i in range(1,max):
            if i not in nums:
                return i

        return max+1
        
