class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        freq = {"a":a,"b":b,"c":c}
        heap = [(-count,character) for character, count in freq.items() if count!=0]
        heapq.heapify(heap)
        res = ""
        while heap:
            if len(res)>1 and res[-1] == res[-2] == heap[0][1]:
                if len(heap)>1:
                    x=heapq.heappop(heap)
                    count,character = heapq.heappop(heap)
                    heapq.heappush(heap,x)
                    count+=1
                else:
                    return res
            else:
                count,character = heapq.heappop(heap)
                count+=1
            res+=character
            if count!=0:
                heapq.heappush(heap,(count,character))
        return res
