from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(Counter(tasks).values())
        queue = deque()
        heap = []
        for fre in freq:
            heapq.heappush(heap,-fre)
        time = 0
        while heap or queue:
            time += 1
            if heap:
                val = heapq.heappop(heap) + 1
                
                if val!=0:
                    queue.append((val,time+n))
                
            
            if queue and time>=queue[0][1]:
                val,v = queue.popleft()
                heapq.heappush(heap,val)
        return time

        