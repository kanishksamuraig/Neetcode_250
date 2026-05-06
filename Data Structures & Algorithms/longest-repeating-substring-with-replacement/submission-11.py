class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length=0;left=0
        dic={}
        for right in range(len(s)):
            dic[s[right]]=1+dic.get(s[right],0)
            max1=max(list(dic.values()))
            while max1+k < right-left+1:
                dic[s[left]]-=1
                max1=max(list(dic.values()))
                left+=1
            length=max(length,right-left+1)
        return length

