import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify_max(nums)
        self.nums=nums[:]
        self.k=k
    def add(self, val: int) -> int:
        heapq.heappush_max(self.nums,val)
        x=[]
        for i in range(self.k):
            val=heapq.heappop_max(self.nums)
            x.append(val)
        for j in range(len(x)):
            heapq.heappush_max(self.nums,x[j])
        return x[-1]


    