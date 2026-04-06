class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[0]*2*len(nums);n=0
        for i in range(len(nums)*2):
            if i>=len(nums):
                n=len(nums)
            ans[i]=nums[i-n]
        return ans