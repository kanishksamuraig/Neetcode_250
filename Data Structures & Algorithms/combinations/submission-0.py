class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst=[]
        def comb(N,K,i,limit,curr):
            if limit==K:
                lst.append(curr.copy())
                return
            
            if i>N:
                return
            
            curr.append(i)
            comb(N,K,i+1,limit+1,curr)
            curr.pop()
            comb(N,K,i+1,limit,curr)
        comb(n,k,1,0,[])
        return lst