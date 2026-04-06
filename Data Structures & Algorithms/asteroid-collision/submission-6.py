class Stack:
    def __init__(self):
        self.stack=[]
        self.top=-1
    def push(self,data:int):
        self.top+=1
        self.stack.append(data)
    def pop(self):
        if self.isempty():
            return -1
        data=self.stack.pop()
        self.top-=1
        return data
    def isempty(self):
        return self.top==-1
    def returnList(self):
        return self.stack.copy()
    def stacktop(self):
        return self.stack[self.top]

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=Stack()
        for index,i in enumerate(asteroids):
            if index==0:
                stack.push(i)
                continue
            flag=True
            while(not stack.isempty() and i<0 and stack.stacktop()>0):
                a=stack.stacktop()
                if abs(i)>a:
                    stack.pop()
                elif abs(i)<a:
                    flag=False
                    break
                else:
                    stack.pop()
                    flag=False
                    break
            if flag:
                stack.push(i)
            


            """while(stack.top>=1):
                a=stack.pop()
                b=stack.pop()
                if a<0 and b>0:
                    condition(stack,a,b)
                else:
                    stack.push(b);stack.push(a)
                    break"""
        return stack.returnList()


            
        