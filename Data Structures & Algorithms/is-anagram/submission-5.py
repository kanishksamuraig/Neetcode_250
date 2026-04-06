class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d={}
        dt={}
        for i in range(len(s)):
            if s[i] not in t or t[i] not in s:
                return False
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1

            if t[i] not in dt:
                dt[t[i]]=1
            else:
                dt[t[i]]+=1
        for i in range(len(s)):
            if d[s[i]]!=dt[s[i]]:
                return False
        return True
            
