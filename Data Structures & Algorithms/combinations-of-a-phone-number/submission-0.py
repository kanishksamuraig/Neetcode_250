class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        lst=[]
        def combinations(curr,index):
            if index==len(digits):
                if len(digits)!=0:
                    lst.append(curr)
                return
            
            for val in d[int(digits[index])]:
                combinations(curr+val,index+1)
            
        combinations("",0)
        return lst