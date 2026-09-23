import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def heapify(heap):
            for curr in range(len(heap)-1,-1,-1):
                while True:
                    largest = curr
                    lchild = 2*curr+1
                    rchild = 2*curr+2
                    if lchild < len(heap) and heap[lchild]>heap[largest]:
                        largest = lchild
                    
                    if rchild < len(heap) and heap[rchild] > heap[largest]:
                        largest = rchild
                    
                    if largest == curr:
                        break
                    
                    heap[largest], heap[curr] = heap[curr], heap[largest]
                    curr = largest
        def push(heap,element):
            heap.append(element)
            curr = len(heap)-1
            while curr > 0 and heap[curr] > heap[(curr-1)//2]:
                heap[curr],heap[(curr-1)//2] = heap[(curr-1)//2],heap[curr]
                curr = (curr-1)//2
        def pop(heap):
            if len(heap)==0:
                return 0
            val = heap[0]
            heap[0] = heap[len(heap)-1]
            heap.pop()
            curr = 0
            while True:
                largest = curr
                lchild = 2*curr+1
                rchild = 2*curr+2

                if lchild < len(heap) and heap[lchild] > heap[largest]:
                    largest = lchild
                if rchild < len(heap) and heap[rchild] > heap[largest]:
                    largest = rchild
                
                if largest == curr:
                    return val
                
                heap[largest],heap[curr] = heap[curr], heap[largest]
                curr = largest
            return val
        heapify(stones)
        while len(stones) >= 2:
            y = pop(stones)
            x = pop(stones)
            if x == y:
                continue
            elif x < y:
                push(stones,y-x)
        return pop(stones)
                    