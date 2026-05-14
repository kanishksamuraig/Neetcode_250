class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dicty={};left=0;maxfreq=0;maxlen=0
        for right in range(len(s)):
            dicty[s[right]]=dicty.get(s[right],0)+1
            maxfreq=max(dicty[s[right]],maxfreq)
            if maxfreq+k < right-left+1:
                dicty[s[left]]-=1
                left+=1
            maxlen=max(right-left+1,maxlen)
        return maxlen