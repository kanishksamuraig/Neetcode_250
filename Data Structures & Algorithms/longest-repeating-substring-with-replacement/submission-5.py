class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maximum=0
        for i in range(len(s)):
            d={}
            for j in range(i,len(s)):
                d[s[j]]=d.get(s[j],0)+1
                for t in d:
                    if ((j-i+1)-d[t])<=k:
                        maximum=max(maximum,j-i+1)
        return maximum 
