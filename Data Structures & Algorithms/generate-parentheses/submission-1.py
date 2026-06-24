class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst=[]
        def paranth(curr,open,close):
            if close>open:
                return
            
            if open + close == 2*n:
                lst.append(curr)
                return
            
            if open < n:
                paranth(curr+"(",open+1,close)
            if close<n:
                paranth(curr+")",open,close+1)
        paranth("",0,0)
        return lst

            