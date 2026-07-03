class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high=max(piles)
        ans=high;low=1
        while low<=high:
            curr=0
            mid = low + (high - low)//2
            for i in range(len(piles)):
                if piles[i]<=mid:
                    curr+=1
                else:
                    curr+=math.ceil(piles[i]/mid)
            if h>=curr:
                ans=mid
                high = mid-1
            else:
                low=mid+1
        return ans
