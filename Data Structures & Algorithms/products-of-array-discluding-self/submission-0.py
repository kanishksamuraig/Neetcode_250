class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        new_arr=[]
        for i in range(len(nums)):
            mul=1
            for j in range(len(nums)):
                if i!=j:
                    mul*=nums[j]
            new_arr.append(mul)
        return new_arr
            
        