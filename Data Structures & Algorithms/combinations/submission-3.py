class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        lst = []
        def combinations(val,n,k,curr):
            if len(curr)==k:
                lst.append(curr.copy())
                return
            if val>n:
                return
            
            curr.append(val)
            combinations(val+1, n, k, curr)
            curr.pop()
            combinations(val+1, n, k, curr)
        combinations(1,n,k,[])
        return lst