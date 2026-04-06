class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pack=list(zip(position,speed))
        pack.sort()
        stack=[]
        for i in pack:
            while stack and ((target-stack[-1][0])/stack[-1][1]<=(target-i[0])/i[1]):
                stack.pop()
            stack.append(i)
        return len(stack)