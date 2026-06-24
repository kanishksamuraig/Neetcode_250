class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lst=[]
        def paranth(curr,open,close):
            
            
            if open + close == 2*n:
                lst.append(curr)
                return
            
            if open < n:
                paranth(curr+"(",open+1,close)
            if close<open:
                paranth(curr+")",open,close+1)
        paranth("",0,0)
        return lst

            