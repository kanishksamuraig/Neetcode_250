class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        container=nums[0]
        for i in nums:
            if i==container:
                count+=1
            else:
                count-=1
                if count==0:
                    container=i
                    count+=1
        return container
            