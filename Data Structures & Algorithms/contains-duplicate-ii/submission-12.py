class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash=set();right=0;left=0
        if k==0:
            return False
        while right<len(nums) and right<=k:
            if nums[right] in hash:
                return True
            hash.add(nums[right])
            right+=1
        right=k
        
        while right<len(nums)-1:
            hash.discard(nums[left])
            left+=1
            right+=1
            if nums[right] in hash:
                return True
            hash.add(nums[right])
        return False