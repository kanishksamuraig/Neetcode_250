class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        def subset(index,sides,target):
            if index == len(matchsticks):
                if sides[0]==sides[1]==sides[2]==sides[3]:
                    return True
                return False
            
            for i in range(4):
                if sides[i]+matchsticks[index]<=target:
                    sides[i]+=matchsticks[index]
                    if subset(index+1,sides,target):
                        return True
                    sides[i] -= matchsticks[index]
                if sides[i]==0:
                    break
            
            return False
        target = sum(matchsticks)
        if target%4!=0:
            return False
        return subset(0,[0,0,0,0],target//4)
