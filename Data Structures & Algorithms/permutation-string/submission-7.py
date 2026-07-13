class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        d1={}
        for i in s1:
            d1[i] = 1 + d1.get(i,0)
        left = 0;right=len(s1)-1;d2={}
        for i in range(len(s1)):
            d2[s2[i]] = 1 + d2.get(s2[i],0)
        if d2==d1:
            return True
        while right<len(s2)-1:
            d2[s2[left]]-=1
            if d2[s2[left]]==0:
                del d2[s2[left]]
            left+=1
            right+=1
            d2[s2[right]] = 1 + d2.get(s2[right],0)
            if d1==d2:
                print(d1,d2)
                print(right,left)
                return True

        return False

