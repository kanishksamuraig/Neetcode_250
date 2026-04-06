class Solution:
    def simplifyPath(self, path: str) -> str:
        i=0;
        stack=[]
        while(i<len(path)):
            if path[i]=="/":
                i+=1
                continue
            ch=""
            while(i<len(path) and (path[i]!="/")):
                ch+=path[i]
                i+=1
            
            if ch[0]==".":
                if len(ch)==2 and stack:
                    stack.pop()
                elif len(ch)>2:
                    stack.append(ch)
            else:
                stack.append(ch)
        stack2=[]
        for i in stack:
            stack2.append("/")
            stack2.append(i)
        return "".join(stack2) if stack2 else "/"



