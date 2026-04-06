class MinStack:

    def __init__(self):
        self.top1=-1
        self.stack=[]
        self.minstack=[]

    def push(self, val: int) -> None:
        if self.top1==-1:
            self.stack.append(val)
            self.minstack.append(val)
            self.top1+=1
            return 
        self.stack.append(val)
        minimum=min(self.minstack[self.top1],val)
        self.minstack.append(minimum)
        self.top1+=1

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        self.top1-=1
        

    def top(self) -> int:
        return self.stack[self.top1]

    def getMin(self) -> int:
        return self.minstack[self.top1]
        
