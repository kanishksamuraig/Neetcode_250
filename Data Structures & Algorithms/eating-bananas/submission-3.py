import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rate=-1;rate2=1
        for i in piles:
            rate=max(i,rate)
        x=0;fin=0
        while rate2<=rate:
            x=0
            mid=rate2+(rate-rate2)//2
            for i in range(len(piles)):
                if piles[i]-mid<=0:
                    x+=1
                else:
                    x+=math.ceil(piles[i]/mid)
            if x<=h:
                fin=mid
                rate=mid-1
            else:
                rate2=mid+1
        return fin
                

