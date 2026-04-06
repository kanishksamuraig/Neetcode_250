class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        suffix=[1]
        for i in range(0,len(nums)-1):
            prefix.append(prefix[i]*nums[i])
            suffix.append(suffix[i]*nums[len(nums)-i-1])
        suffix=suffix[::-1]
        product=[]
        for i in range(len(prefix)):
            product.append(prefix[i]*suffix[i])
        return product


