class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[];l=0;top=-1
        while(l<len(temperatures)):
            top+=1
            stack.append(temperatures[l])
            r=l+1;flag=False
            while(r<len(temperatures)):
                if temperatures[r]>temperatures[l]:
                    flag=True
                    res.append(r-l)
                    break
                r+=1
            if not flag:
                res.append(0)
            l+=1
        return res
                
