class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word=strs[0]
        j=len(word)
        for i in range(1,len(strs)):
            if len(strs[i])<j:
                j=len(strs[i])
            while(strs[i][:j]!=word[:j]):
                j-=1
                if j==0:
                    return ""
        return word[:j]