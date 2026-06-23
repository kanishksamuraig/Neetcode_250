class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst=[]
        def comb(n,k,i,curr):
            if k==0:
                lst.append(curr.copy())
                return
            
            if i>n:
                return
            
            curr.append(i)
            comb(n,k-1,i+1,curr)
            curr.pop()
            comb(n,k,i+1,curr)
        comb(n,k,1,[])
        return lst