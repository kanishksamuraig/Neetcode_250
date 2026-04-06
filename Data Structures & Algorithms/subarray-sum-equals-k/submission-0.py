class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentsum=0
        prefixsum={0:1}
        count=0
        for num in nums:
            currentsum+=num
            diff=currentsum-k
            if diff in prefixsum:
                count+=prefixsum[diff]
            prefixsum[currentsum]=1+prefixsum.get(currentsum,0)
        return count