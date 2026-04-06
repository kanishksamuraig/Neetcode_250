class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum=len(nums);left=0;right=0
        sum1=0;flag=False
        while right<len(nums):
            sum1=sum1+nums[right]

            while sum1>=target:
                minimum=min(minimum,right-left+1)
                flag=True
                sum1-=nums[left]
                left+=1
            right+=1
        return minimum if flag else 0