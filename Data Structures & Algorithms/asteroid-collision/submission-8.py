class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(len(asteroids)):
            flag=True
            while stack and asteroids[i]<0 and stack[-1]>0:
                if stack[-1]<abs(asteroids[i]):
                    stack.pop()
                    flag=True
                elif stack[-1]==abs(asteroids[i]):
                    stack.pop()
                    flag=False
                    break
                else:
                    flag=False
                    break
            if flag:
                stack.append(asteroids[i])
        return stack