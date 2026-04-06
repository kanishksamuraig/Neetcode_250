class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common=strs[0]
        j=len(common)
        for i in range(1,len(strs)):
            if j>len(strs[i]):
                j=len(strs[i])
            while common[:j]!=strs[i][:j]:
                j-=1
                if j==0:
                    return ""
            common=common[:j]
        return common
            