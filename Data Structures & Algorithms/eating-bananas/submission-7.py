class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high=max(piles)
        ans=high;low=1
        while low<=high:
            curr=0
            mid = low + (high - low)//2
            for i in range(len(piles)):
                curr+=(piles[i]+mid-1)//mid
            if h>=curr:
                ans=mid
                high = mid-1
            else:
                low=mid+1
        return ans
