class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alpha1,alpha2={},{}
        if len(s1)>len(s2):
            return False
        for i in range(26):
            alpha1[chr(i+97)]=0
            alpha2[chr(i+97)]=0
        total1=0;total2=0
        for i in range(len(s1)):
            total1+=ord(s1[i])-96
            alpha1[s1[i]]+=1
            alpha2[s2[i]]+=1
            total2+=ord(s2[i])-96
        left=0;right=len(s1)-1
        if total1==total2:
            if alpha1==alpha2:
                return True
        while right<len(s2)-1:
            total2-=ord(s2[left])-1
            alpha2[s2[left]]-=1
            left+=1
            right+=1
            alpha2[s2[right]]+=1
            total2+=ord(s2[right])-1
            if total1==total2:
                if alpha1==alpha2:
                    return True

        return False

        