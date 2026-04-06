class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[];top=-1
        for element in operations:
            if element=="C":
                stack.pop()
                top-=1
            elif element=="+":
                sum=stack[top]+stack[top-1]
                stack.append(sum)
                top+=1
            elif element=="D":
                mul=stack[top]*2
                stack.append(mul)
                top+=1
            else:
                stack.append(int(element))
                top+=1
        sum=0
        for i in stack:
            sum+=i
        return sum