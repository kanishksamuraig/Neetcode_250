class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1;high=max(piles);res=0
        while low<=high:
            rate=low+(high-low)//2;hours=0
            for i in range(len(piles)):
                if piles[i]<=rate:
                    hours+=1
                else:
                    hours+=math.ceil(piles[i]/rate)
            if hours<=h:
                res=rate
                high=rate-1
            else:
                low=rate+1
        return res