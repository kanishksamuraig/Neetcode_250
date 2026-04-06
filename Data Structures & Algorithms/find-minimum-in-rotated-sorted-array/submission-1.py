class Solution:
    def findMin(self, nums: List[int]) -> int:
        res=nums[0]
        low=0;high=len(nums)-1
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]<res:
                res=nums[mid]
            if nums[low]<=nums[high]:
                if nums[low]<res:
                    res=nums[low]
                return res
            elif nums[low]<=nums[mid]:
                low=mid+1
            else:
                high=mid-1
        return res
            