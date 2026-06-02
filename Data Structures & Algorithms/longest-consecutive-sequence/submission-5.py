class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique=set(nums);maxlen=0
        for i in unique:
            length=0
            while length+i in unique:
                length+=1
            maxlen=max(length,maxlen)
        return maxlen













        
