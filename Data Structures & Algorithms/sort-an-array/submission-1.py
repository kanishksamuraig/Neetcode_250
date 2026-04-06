class Solution:
    def mergeSort(self,nums,length):
        if length<=1:
            return
        middle=length//2
        left=[];right=[]
        for i in range(length):
            if i<middle:
                left.append(nums[i])
            else:
                right.append(nums[i])
        self.mergeSort(left,middle)
        self.mergeSort(right,length-middle)
        self.merge(left,right,nums,length)

    def merge(self,left,right,nums,length):
        leftsize=length//2;rightsize=length-leftsize;l=0;r=0;i=0
        while(l<leftsize and r<rightsize):
            if left[l]>right[r]:
                nums[i]=right[r]
                i+=1
                r+=1
            else:
                nums[i]=left[l]
                i+=1
                l+=1
        while(r<rightsize):
            nums[i]=right[r]
            i+=1
            r+=1
        while(l<leftsize):
            nums[i]=left[l]
            i+=1
            l+=1
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums,len(nums))
        return nums
        