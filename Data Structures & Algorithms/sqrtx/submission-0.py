class Solution:
    def mySqrt(self, x: int) -> int:
        low=0;high=x;target=int(x**0.5)
        while low<=high:
            mid=low+(high-low)//2
            if mid==target:
                return mid
            elif mid<target:
                low=mid+1
            else:
                high=mid-1
            