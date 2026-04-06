class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        container=nums[0]
        count=1
        for i in range(1,len(nums)):
            if container!=nums[i]:
                count-=1
                if count==0:
                    container=nums[i]
                    count=1
            else:
                count+=1
        return container