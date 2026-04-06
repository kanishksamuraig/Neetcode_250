class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights);res=0
        high=low*len(weights)
        while low<=high:
            mid=low+(high-low)//2;w=mid;day=1
            for i in range(len(weights)):
                if weights[i]<=w:
                    w-=weights[i]
                else:
                    w=mid
                    w-=weights[i]
                    day+=1
            if day<=days:
                high=mid-1
                res=mid
            else:
                low=mid+1
        return res

                