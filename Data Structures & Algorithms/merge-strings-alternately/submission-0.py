class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index1=0
        index2=0
        res=""
        while(index1<len(word1) and index2<len(word2)):
            res+=word1[index1]
            res+=word2[index2]
            index1+=1
            index2+=1
        while(index1<len(word1)):
            res+=word1[index1]
            index1+=1
        while(index2<len(word2)):
            res+=word2[index2]
            index2+=1
        return res
            
