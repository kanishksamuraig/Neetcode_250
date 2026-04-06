class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        maxsize=0
        for n in nums:
            length=0
            if n-1 not in numset:
                while(n+length in numset):
                    length+=1
            maxsize=max(length,maxsize)
        return maxsize 

        