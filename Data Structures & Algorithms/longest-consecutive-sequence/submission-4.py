class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums);maxlen=0
        for num in numset:
            if num-1 not in numset:
                length=0
                while(num+length in numset):
                    length+=1
                maxlen=max(length,maxlen)
        return maxlen