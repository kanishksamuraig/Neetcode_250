import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            val = x**2 + y**2
            heapq.heappush(heap,(-val,(x,y)))
            if len(heap)>k:
                heapq.heappop(heap)
        return [x for val,x in heap]