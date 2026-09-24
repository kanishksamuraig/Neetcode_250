class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        lst = []
        def sub(curr,index):
            if index==len(nums):
                lst.append(curr.copy())
                return
            
            curr.append(nums[index])
            sub(curr,index+1)
            curr.pop()
            sub(curr,index+1)
        sub([],0)
        return lst
