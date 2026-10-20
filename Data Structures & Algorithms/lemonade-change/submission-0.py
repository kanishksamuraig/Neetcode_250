class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5:0,10:0,20:0};l = [20,10,5]
        for i in range(len(bills)):
            curr = bills[i]
            d[curr] += 1
            i = 0
            while curr > 5 and i < 3:
                if curr - l[i] >= 5 and d[l[i]]>0:
                    d[l[i]]-=1
                    curr -= l[i]
                else:
                    i += 1  
            if i==3:
                return False

            

        return True