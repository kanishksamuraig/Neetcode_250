class maxheap:
    def __init__(self, nums):
        self.nums = nums[:]
        for i in range(len(nums) - 1, -1, -1):
            curr = i
            while True:
                largest = curr
                lchild = 2 * curr + 1
                rchild = 2 * curr + 2

                if lchild < len(self.nums) and self.nums[lchild] > self.nums[largest]:
                    largest = lchild

                if rchild < len(self.nums) and self.nums[rchild] > self.nums[largest]:
                    largest = rchild

                if curr == largest:
                    break

                self.nums[curr], self.nums[largest] = self.nums[largest], self.nums[curr]
                curr = largest

    def push(self, val):
        self.nums.append(val)
        curr = len(self.nums) - 1
        while curr > 0 and self.nums[curr] > self.nums[(curr - 1) // 2]:
            self.nums[curr], self.nums[(curr - 1) // 2] = (
                self.nums[(curr - 1) // 2],
                self.nums[curr],
            )
            curr = (curr - 1) // 2

    def pop(self):
        if len(self.nums)==0:
            return 0
        val = self.nums[0]
        self.nums[0] = self.nums[len(self.nums) - 1]
        curr = 0
        self.nums.pop()
        while True:
            largest = curr
            lchild = 2 * curr + 1
            rchild = 2 * curr + 2

            if lchild < len(self.nums) and self.nums[lchild] > self.nums[largest]:
                largest = lchild

            if rchild < len(self.nums) and self.nums[rchild] > self.nums[largest]:
                largest = rchild

            if largest == curr:
                return val

            self.nums[largest], self.nums[curr] = self.nums[curr], self.nums[largest]
            curr = largest
    def peek(self):
        return self.nums[0]
    def __len__(self):
        return len(self.nums)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = maxheap(stones)
        while len(heap) > 1:
            y=heap.pop()
            x=heap.pop()
            if x < y:
                heap.push(y-x)
        return heap.pop()


