class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        def maxfreq(d):
            freq=0;majority=""
            for i in d:
                if d[i]>freq:
                    freq=d[i]
                    majority=i
            return (freq,majority)
        right=0;left=0;d={};maximum=0
        while right<len(s):
            d[s[right]]=d.get(s[right],0)+1
            if (right-left+1-maxfreq(d)[0])>k:
                d[s[left]]-=1
                left+=1
            maximum=max(maximum,right-left+1)
            right+=1
        return maximum    
            
            