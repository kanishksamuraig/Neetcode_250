class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i,n in enumerate(nums):
            if target-n in dict1:
                return [dict1[target-n],i]
            dict1[n]=i


