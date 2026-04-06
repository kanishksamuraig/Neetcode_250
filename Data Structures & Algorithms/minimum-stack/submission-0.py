class MinStack:

    def __init__(self):
        self.stack=[]    
        self.top1=-1
        self.minstack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.top1+=1
    def pop(self) -> None:
        self.top1-=1
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[self.top1]

    def getMin(self) -> int:
        return min(self.stack)
        
