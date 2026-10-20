class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = {5:0,10:0,20:0};l = [20,10,5]
        for i in range(len(bills)):
            curr = bills[i]
            d[curr] += 1
            j = 0
            while curr > 5 and j < 3:
                if curr - l[j] >= 5 and d[l[j]]>0:
                    d[l[j]]-=1
                    curr -= l[j]
                else:
                    j += 1  
            if j==3:
                return False

            

        return True