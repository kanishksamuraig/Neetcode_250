class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1 = 0
        maxsum = -10001
        for i in range(len(nums)):
            sum1 += nums[i]
            maxsum = max(sum1,maxsum)
            if sum1 < 0:
                sum1 = 0
        return maxsum