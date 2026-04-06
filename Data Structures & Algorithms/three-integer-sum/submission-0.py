class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out=[]
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k]==0 and sorted([nums[i],nums[j],nums[k]]) not in out:
                        out.append(sorted([nums[i],nums[j],nums[k]]))
        return out