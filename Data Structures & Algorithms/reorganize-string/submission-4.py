class Solution:
    def reorganizeString(self, s: str) -> str:
        freq={}
        for i in s:
            freq[i] = 1 + freq.get(i,0)
        count=0
        for i in freq:
            count+=1
            if freq[i]>(len(s)+1)/2:
                return ""
        res=""
        while count>0:
            max1=(-1,-1)
            for i in freq:
                if max1[0]<freq[i]:
                    max1=(freq[i],i)
            max2=(-1,-1)
            for i in freq:
                if max2[0]<freq[i] and i!=max1[1]:
                    max2=(freq[i],i)
            if max2[0]!=-1:
                res+=max1[1]+max2[1]
                freq[max1[1]]-=1
                freq[max2[1]]-=1
                if freq[max1[1]]==0:
                    del freq[max1[1]]
                    count-=1
                if freq[max2[1]]==0:
                    del freq[max2[1]]
                    count-=1
            else:
                res+=max1[1]
                freq[max1[1]]-=1
                
                if freq[max1[1]]==0:
                    del freq[max1[1]]
                    count-=1
        return res

