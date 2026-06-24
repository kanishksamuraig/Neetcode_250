class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        lst=[];nums.sort()
        def perm(curr,hash):
            if len(curr)==len(nums):
                lst.append(curr.copy())
                return
            index=0
            while index < len(nums):
                if index not in hash:
                    curr.append(nums[index])
                    hash.add(index)
                    perm(curr,hash)
                    hash.remove(index)
                    curr.pop()
                    
                    while index<len(nums)-1 and nums[index]==nums[index+1]:
                        index+=1
                index+=1
        perm([],set())
        return lst
