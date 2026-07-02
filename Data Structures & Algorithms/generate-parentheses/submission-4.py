class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst=[]
        def genpar(curr,open,close,n):
            if len(curr)==2*n:
                lst.append(curr)
            
            if open<n:
                genpar(curr+"(",open+1,close,n)
            
            if close<open:
                genpar(curr+")",open,close+1,n)
        
        genpar("",0,0,n)
        return lst