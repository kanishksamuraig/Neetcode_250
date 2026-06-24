class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        lst=[];hash=set()
        def perm(hash,curr,i):
            if i==len(nums):
                lst.append(curr[:])
                return
            for index in range(len(nums)):
                if nums[index%(len(nums))] not in hash:
                    curr.append(nums[index%(len(nums))]) 
                    hash.add(nums[index%(len(nums))])
                    perm(hash,curr,i+1)
                    curr.pop()
                    hash.remove(nums[index%len(nums)])
            
        perm(hash,[],0)
        return lst

            


            

            

            