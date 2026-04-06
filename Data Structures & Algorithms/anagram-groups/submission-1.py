class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(string1,string2):
            if len(string1)!=len(string2):
                return False
            dict1={}
            dict2={}
            for i in range(len(string1)):
                if string1[i] not in string2 or string2[i] not in string1:
                    return False 
                if string1[i] not in dict1:
                    dict1[string1[i]]=1
                else:
                    dict1[string1[i]]+=1
                
                if string2[i] not in dict2:
                    dict2[string2[i]]=1
                else:
                    dict2[string2[i]]+=1
            if dict1!=dict2:
                return False
            return True
        l=[]
        flag=[False for _ in range(len(strs))]
        print(flag)
        for i in range(len(strs)):
            temp=[]
            if not flag[i]:
                temp.append(strs[i])
                flag[i]=True
                for j in range(i,len(strs)):
                    if isAnagram(strs[i],strs[j]) and not flag[j]: 
                        temp.append(strs[j])
                        flag[j]=True
                l.append(temp)
        return l
                