class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i].isnumeric():
                if stack and stack[-1].isnumeric():
                    n=stack.pop()
                    stack.append(n+s[i])
                else:
                    stack.append(s[i])
            elif s[i].isalpha():
                if stack and stack[-1].isalpha():
                    n=stack.pop()
                    stack.append(n+s[i])
                else:
                    stack.append(s[i])
            elif s[i]=="]":
                string=""
                while stack and not stack[-1]=="[":
                    string=stack.pop()+string
                stack.pop()
                n=int(stack.pop())
                stack.append(n*string)
            else:
                stack.append(s[i])
            print(stack)
        string=""
        while stack:
            string=stack.pop()+string
        return string