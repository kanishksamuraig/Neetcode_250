class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lst=[0]*2*len(nums);k=0
        for i in range(2*len(nums)):
            if i==len(nums):
                k=len(nums)
            lst[i] = nums[i-k]
        return lst