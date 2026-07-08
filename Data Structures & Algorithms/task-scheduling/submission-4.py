import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq={};heap=[]
        for i in tasks:
            freq[i] = 1 + freq.get(i,0)
        queue=deque()
        for i in freq:
            heapq.heappush_max(heap,freq[i])
        time=0
        while heap or queue:  
            if not heap:
                if queue and time < queue[0][1]:
                    time = queue[0][1]
                      
            if heap:
                val=heapq.heappop_max(heap)-1
                time += 1
                if val!=0:
                    queue.append((val,time+n))

            
            
            
            if queue and time >= queue[0][1]:
                heapq.heappush_max(heap,queue.popleft()[0])
        return time

