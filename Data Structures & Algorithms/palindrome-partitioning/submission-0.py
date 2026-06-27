class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispali(word):
            left=0;right=len(word)-1
            while left<=right:
                if word[left]!=word[right]:
                    return False
                left+=1
                right-=1
            return True

        lst=[]
        def substring(curr,start):
            if start==len(s):
                lst.append(curr[:])
                return
            
            for i in range(start+1,len(s)+1):
                if ispali(s[start:i]):
                    curr.append(s[start:i])
                    substring(curr,i)
                    curr.pop()
        substring([],0)
        return lst
            
