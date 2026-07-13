class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        maxprofit=0;l=0
        for r in range(len(nums)):
            if nums[l]>nums[r]:
                l = r
                continue
            profit = nums[r]-nums[l]
            maxprofit = max(maxprofit,profit)
        return maxprofit