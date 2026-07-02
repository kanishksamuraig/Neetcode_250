class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        lst=[]
        def permutation(hash,curr):
            if len(curr)==len(nums):
                lst.append(curr[:])
                return

            for i in range(len(nums)):
                if nums[i] not in hash:
                    hash.add(nums[i])
                    curr.append(nums[i])
                    permutation(hash,curr)
                    curr.pop()
                    hash.remove(nums[i])
        
        permutation(set(),[])
        return lst

