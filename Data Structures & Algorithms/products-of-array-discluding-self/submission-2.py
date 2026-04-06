class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        suffix=[1]
        mul=1
        
        for i in range(len(nums)-1):
            mul*=nums[i]
            prefix.append(mul)
        mul=1
        for i in range(len(nums)-1,0,-1):
            mul*=nums[i]
            suffix.append(mul)
        suffix.reverse()
        new_arr=[]
        for i in range(len(nums)):
            new_arr.append(suffix[i]*prefix[i])
        return new_arr