class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def mergeSort(keys,values,length):
            if length<=1:
                return
            leftkeys=[]
            rightkeys=[]
            leftvalues=[]
            rightvalues=[]
            middle=length//2
            j=0
            for i in range(length):
                if i<middle:
                    leftvalues.append(values[i])
                    leftkeys.append(keys[i])
                else:
                    rightvalues.append(values[i])
                    rightkeys.append(keys[i])
            
            mergeSort(leftkeys,leftvalues,middle)
            mergeSort(rightkeys,rightvalues,length-middle)
            merge(leftvalues,rightvalues,values,leftkeys,rightkeys,keys,length)
        
        def merge(leftvalues,rightvalues,values,leftkeys,rightkeys,keys,length):
            leftsize=length//2
            rightsize=length-leftsize;r=0;l=0;i=0
            while l<leftsize and r<rightsize:
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
            while r<rightsize:
                values[i]=rightvalues[r]
                keys[i]=rightkeys[r]
                i+=1
                r+=1
            while l<leftsize:
                values[i]=leftvalues[l]
                keys[i]=leftkeys[l]
                i+=1
                l+=1
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        keys=[]
        values=[]
        for i in d:
            keys.append(i)
            values.append(d[i])
        mergeSort(keys,values,len(keys))
        print(keys,values)
        t=[]
        for i in range(len(values)-1,len(values)-1-k,-1):
            t.append(keys[i])
        return t

        
