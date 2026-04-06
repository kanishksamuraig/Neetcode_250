class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i in range(len(nums)):
            if (target-nums[i]) in dict1:
                return sorted([i,nums.index(target-nums[i])])
            dict1[nums[i]]=target-nums[i]
        return None