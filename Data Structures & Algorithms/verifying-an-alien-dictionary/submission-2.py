class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash={}
        for index,alpha in enumerate(order,1):
            hash[alpha]=index
        for i in range(1,len(words)):
            flag=False
            word2=words[i];word1=words[i-1]
            for j in range(min(len(words[i]),len(words[i-1]))):
                if hash[word2[j]] < hash[word1[j]]:
                    return False
                elif hash[word2[j]]>hash[word1[j]]:
                    flag=True
                    break
            if not flag:
                if len(word1)>len(word2):
                    return False 
        return True

