class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target = sum(nums)
        if target%k!=0:
            return False
        res=[0 for _ in range(k)]
        nums.sort(reverse=True)
        def perm(res,index,target):
            if index==len(nums):
                print(res)
                return True
            
            for i in range(len(res)):
                if res[i]+nums[index]<=target:
                    res[i]+=nums[index]
                    if perm(res,index+1,target):
                        return True
                    res[i]-=nums[index]
                
                if res[i]==0:
                    break
            return False
        return perm(res,0,target//k)
