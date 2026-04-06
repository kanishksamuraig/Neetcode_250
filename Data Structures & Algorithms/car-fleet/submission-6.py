class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet=len(position)
        car=list(zip(position,speed))
        cars=sorted(car,key=lambda x: x[0],reverse=True)
        stack=[]
        for car in cars:
            stack.append((target-car[0])/car[1])
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
            
        return len(stack)