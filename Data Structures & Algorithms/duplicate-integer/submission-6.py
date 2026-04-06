class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashey={}
        for i in range(len(nums)):
            if nums[i] not in hashey:
                hashey[nums[i]]=1
            else:
                return True
        return False
