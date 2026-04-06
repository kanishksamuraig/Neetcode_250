class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        visited=[False for _ in range(len(strs))]
        for i in range(len(strs)):
            if not visited[i]:
                d1={}
                word=strs[i]
                l=[]
                visited[i]=True
                l.append(word)
                for j in range(len(word)):
                    if word[j] not in d1:
                        d1[word[j]]=1
                    else:
                        d1[word[j]]+=1
                for j in range(i+1,len(strs)):
                    d2={}
                    if not visited[j] and len(word)==len(strs[j]):
                        word2=strs[j]
                        for k in range(len(word2)):
                            if word2[k] not in d2:
                                d2[word2[k]]=1
                            else:
                                d2[word2[k]]+=1
                        if d1==d2:
                            visited[j]=True
                            l.append(word2)
                res.append(l)
        return res
                        




