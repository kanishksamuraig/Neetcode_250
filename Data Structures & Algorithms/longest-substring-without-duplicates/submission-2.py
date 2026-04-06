class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0;r=0;hashset=set();maxlen=0
        while(r<len(s)):
            while(s[r] in hashset):
                hashset.remove(s[l])
                l+=1
            
            if s[r] not in hashset:
                maxlen=max(maxlen,r-l+1)
                hashset.add(s[r])
                r+=1
        return maxlen
