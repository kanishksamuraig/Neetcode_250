class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        for i in range(len(s)):
            ch=s[i]
            if ch=="(" or ch=="{" or ch=="[":
                stack.append(ch)
                top+=1
            elif len(stack)>0:
                if (ch==")" and stack[top]!="(") or (ch=="}" and stack[top]!="{") or (ch=="]" and stack[top]!="["):
                    return False
                else:
                    stack.pop()
                    top-=1
            else:
                return False
        return len(stack)==0


            
