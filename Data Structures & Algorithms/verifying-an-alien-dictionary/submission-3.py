class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash={}
        for index,alpha in enumerate(order,1):
            hash[alpha]=index
        for i in range(1,len(words)):
            word2=words[i];word1=words[i-1]
            j=0
            while j<min(len(word1),len(word2)) and word2[j]==word1[j]:
                j+=1
            if j<min(len(word1),len(word2)):
                if hash[word1[j]]>hash[word2[j]]:
                    return False
            if j==min(len(word1),len(word2)):
                if len(word1)>len(word2):
                    return False


        return True

