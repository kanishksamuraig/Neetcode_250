class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring="";maxlen=0
        for i in range(len(s)):
            hashset=set()
            for j in range(i,len(s)):
                if s[j] not in hashset:
                    if j-i+1>maxlen:
                        maxlen=j-i+1
                        substring=s[i:j+1]
                    hashset.add(s[j])
                else:
                    break
        return maxlen



                