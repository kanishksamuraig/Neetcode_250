class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if nums.count(nums[i])>1:
                return True
        return False