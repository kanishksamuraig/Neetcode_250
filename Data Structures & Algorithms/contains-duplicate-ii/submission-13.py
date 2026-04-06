class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash=set();left=0;right=0
        while right<len(nums) and right<=k:
            if nums[right] in hash:
                return True
            hash.add(nums[right])
            right+=1
        right-=1
        while right<len(nums)-1:
            hash.remove(nums[left])
            left+=1
            right+=1
            if nums[right] in hash:
                return True
            hash.add(nums[right])
        return False            
