class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.capacity = k
        self.heap=nums[:]
        self.size=len(nums)
        heapq.heapify(self.heap)
        while self.size > self.capacity:
            heapq.heappop(self.heap)
            self.size-=1
    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        self.size+=1
        if self.size > self.capacity:
            heapq.heappop(self.heap)
            self.size-=1
        return self.heap[0]


