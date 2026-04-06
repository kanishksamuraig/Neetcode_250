class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j=len(strs[0])
        prefix=strs[0]
        for i in range(1,len(strs)):
            string=strs[i]
            j=min(len(string),len(prefix))
            while(j>0 and string[:j]!=prefix[:j]):
                j-=1
                if j==0:
                    return ""
            prefix=string[:j]
        return prefix