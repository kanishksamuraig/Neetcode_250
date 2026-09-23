from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = list(count.values())
        for i in range(len(heap)):
            heap[i] = -heap[i]
        heapq.heapify(heap)
        print(heap)
        queue = deque()
        time = 0
        while heap or queue:
            time +=1
            if heap:
                freq = heapq.heappop(heap)+1
                if freq!=0:
                    queue.append((freq,time+n))
                
            if queue and time==queue[0][1]:
                freq,time = queue.popleft() 
                heapq.heappush(heap,freq)
            
        return time

        