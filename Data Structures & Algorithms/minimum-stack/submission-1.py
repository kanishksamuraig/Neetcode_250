class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        self.top1=-1

    def push(self, val: int) -> None:
        self.stack.append(val)
        temp=[]
        t=self.top1
        while(t>=0 and val>self.minstack[t]):
            temp.append(self.minstack.pop())
            t-=1
        self.minstack.append(val)
        while(temp):
            self.minstack.append(temp.pop())
        self.top1+=1

    def pop(self) -> None:
        data=self.stack.pop()
        temp=[];t=self.top1
        while(t>=0 and data!=self.minstack[t]):
            temp.append(self.minstack.pop())
            t-=1
        self.minstack.pop()
        while(temp):
            self.minstack.append(temp.pop())
        self.top1-=1
        

    def top(self) -> int:
        return self.stack[self.top1]

    def getMin(self) -> int:
        return self.minstack[self.top1]
        
        
