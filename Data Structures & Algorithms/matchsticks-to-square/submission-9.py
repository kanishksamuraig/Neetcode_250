class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sum1=sum(matchsticks)
        if sum1%4!=0:
            return False
        matchsticks.sort(reverse=True)
        methed=[0,0,0,0]
        def meth(index,target):
            if index==len(matchsticks):
                return True
            flag=False
            for i in range(4):
                if matchsticks[index]+methed[i]<=target:
                    methed[i]+=matchsticks[index]
                    if meth(index+1,target):
                        return True
                    methed[i]-=matchsticks[index]
                
                if methed[i]==0:
                    return False
            return False
        return meth(0,sum1//4)
            
            