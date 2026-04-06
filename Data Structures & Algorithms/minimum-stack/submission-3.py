class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self, val: int) -> None:
        if not self.minstack:
            self.minstack.append(val)
            self.stack.append(val)
            return 
        elif self.minstack[-1]>val:
            self.minstack.append(val)
            self.stack.append(val)
            return
        self.minstack.append(self.minstack[-1])
        self.stack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minstack[-1]
