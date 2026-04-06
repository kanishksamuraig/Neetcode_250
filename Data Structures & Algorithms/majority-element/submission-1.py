class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        n=0
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
            if d[nums[i]]> len(nums)//2:
                n=nums[i]
                break
        return n
                