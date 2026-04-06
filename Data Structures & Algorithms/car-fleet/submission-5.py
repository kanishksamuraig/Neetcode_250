class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet=len(position)
        car=list(zip(position,speed))
        cars=sorted(car,key=lambda x: x[0])
        stack=[]
        for car in cars:
            while stack and stack[-1]<=(target-car[0])/car[1]:
                stack.pop()
            stack.append((target-car[0])/car[1])
        return len(stack)