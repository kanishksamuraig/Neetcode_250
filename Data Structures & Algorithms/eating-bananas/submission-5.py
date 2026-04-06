class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1;right=-float('inf');res=right*h
        for i in piles:
            if i>right:
                right=i
        while left<=right:
            mid=left+(right-left)//2
            count=0
            for i in range(len(piles)):
                if (piles[i]-mid)<=0:
                    count+=1
                else:
                    count+=math.ceil(piles[i]/mid)
            if count>h:
                left=mid+1
            else:
                res=mid
                right=mid-1
        return res