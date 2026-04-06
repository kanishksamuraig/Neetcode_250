class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i in range(len(nums)):
            if target-nums[i] in dict1 and dict1[target-nums[i]]!=i:
                return [min(i,dict1[target-nums[i]]),max(i,dict1[target-nums[i]])]
            dict1[nums[i]]=i
        