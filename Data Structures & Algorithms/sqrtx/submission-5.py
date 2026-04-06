class Solution:
    def mySqrt(self, x: int) -> int:
        low=0;high=x;res=0
        while low<=high:
            mid=low+(high-low)//2
            if mid*mid==x:
                return int(mid)
            elif mid*mid<x:
                low=mid+1
                res=mid
            else:
                high=mid-1
        return int(res)