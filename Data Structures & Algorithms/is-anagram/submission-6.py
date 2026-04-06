class Solution:
    def isAnagram(self,string1:str,string2:str)->bool:
        dict1={}
        dict2={}

        if len(string1)!=len(string2):
            return False
        
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
        