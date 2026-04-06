class Solution:
    def reverse(self,nums,left,right):
        l=left;r=right-1
        while(l<=r):
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        self.reverse(nums,0,len(nums))
        self.reverse(nums,0,k)
        self.reverse(nums,k,len(nums))
        