class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0;fast=1
        while nums[slow]!=nums[fast]:
            slow=(slow+1)%len(nums)
            fast=(fast+2)%len(nums)
            if fast==slow:
                fast=(slow+1)%len(nums)
        return nums[slow]


