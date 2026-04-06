class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def mergeSort(values,keys,length):
            if length<=1:
                return 
            middle=length//2;j=0
            leftkeys=[];rightkeys=[]
            leftvalues=[];rightvalues=[]
            for i in range(length):
                if i<middle:
                    leftkeys.append(keys[i])
                    leftvalues.append(values[i])
                else:
                    rightkeys.append(keys[i])
                    rightvalues.append(values[i])
                    j+=1
            mergeSort(leftvalues,leftkeys,middle)
            mergeSort(rightvalues,rightkeys,length-middle)
            merge(leftvalues,leftkeys,rightvalues,rightkeys,values,keys,length)
        
        def merge(leftvalues,leftkeys,rightvalues,rightkeys,values,keys,length):
            i=0;r=0;l=0;leftsize=length//2;rightsize=length-leftsize
            while (l<leftsize and r<rightsize):
                if leftvalues[l]<rightvalues[r]:
                    values[i]=leftvalues[l]
                    keys[i]=leftkeys[l]
                    i+=1
                    l+=1
                else:
                    values[i]=rightvalues[r]
                    keys[i]=rightkeys[r]
                    i+=1
                    r+=1
            while (r<rightsize):
                values[i]=rightvalues[r]
                keys[i]=rightkeys[r]
                i+=1
                r+=1
            while l<leftsize:
                values[i]=leftvalues[l]
                keys[i]=leftkeys[l]
                i+=1
                l+=1


        
        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        keys=[]
        values=[]
        for i in dict1:
            keys.append(i)
            values.append(dict1[i])
        mergeSort(values,keys,len(keys))
        res=[]
        for i in range(len(keys)-1,len(keys)-1-k,-1):
            res.append(keys[i])
        return res
