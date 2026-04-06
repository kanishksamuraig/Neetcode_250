class Solution:
    def decodeString(self, s: str) -> str:
        stack=[];string=""
        for i in s:
            if i!="]":
                if stack and stack[-1].isnumeric() and i.isnumeric():
                    stack.append(stack.pop()+i)
                else:
                    stack.append(i)
                continue
            ch=""
            while stack and stack[-1]!="[":
                ch=stack.pop()+ch
            stack.pop()
            if stack and stack[-1].isnumeric():
                n=int(stack.pop())
                ch*=n
                stack.append(ch)
            elif stack and stack[-1].isalpha():
                stack.append(stack.pop()+ch)
            else:
                stack.append(ch)
        restack=[]
        while stack:
            restack.append(stack.pop())
        while restack:
            string+=restack.pop()
        return string
            