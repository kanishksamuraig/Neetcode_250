
class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class MyCircularQueue:

    def __init__(self, k: int):
        self.tail=None;
        self.head=None;
        self.size=0;
        self.k=k;
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        elif self.isEmpty():
            self.head=Node(value)
            self.tail=self.head
        else:
            self.tail.next=Node(value)
            self.tail=self.tail.next
        self.size+=1
        self.tail.next=self.head
        return True
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        elif self.head==self.tail:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.tail.next=self.head
        self.size-=1
        return True
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val
        

    def isEmpty(self) -> bool:
        if self.size==0:
            return True
        return False
    def isFull(self) -> bool:
        if self.size==self.k:
            return True
        return False
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()