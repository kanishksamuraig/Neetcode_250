class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash={0:1}
        sum=0;count=0
        for i in range(len(nums)):
            sum+=nums[i]
            diff=sum-k
            if diff in hash:
                count+=hash[diff]
            hash[sum]=1+hash.get(sum,0)
        return count
