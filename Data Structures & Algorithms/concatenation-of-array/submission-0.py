class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        s=[0]*len(nums)*2
        n=0
        for i in range(2*len(nums)):
            s[i]=nums[i-n]
            if i==len(nums)-1:
                n=len(nums)

        return s

        