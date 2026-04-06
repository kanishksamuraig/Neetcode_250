class Stack:
    def __init__(self):
        self.stack=[]
        self.top=-1
    def push(self,data):
        self.top+=1
        self.stack.append(data)
    def pop(self):
        x=self.stack.pop()
        self.top-=1
        return x
    def isempty(self):
        if self.top==-1:
            return True
        return False
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=Stack()
        for i in tokens:
            if i=="+":
                a=stack.pop();b=stack.pop()
                stack.push(a+b)
            elif i=="-":
                a=stack.pop();b=stack.pop()
                stack.push(b-a)
            elif i=="*":
                a=stack.pop();b=stack.pop()
                stack.push(a*b)
            elif i=="/":
                a=stack.pop();b=stack.pop()
                stack.push(-(-b//a) if a<0 or b<0 else b//a)
            else:
                stack.push(int(i))
        return stack.pop()

        