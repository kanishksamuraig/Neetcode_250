class Solution:
    def subsets(self, arr):
        # code here
        lst=[];currentlist=[]
        def sets(length,index,currentlist):
            nonlocal lst
            if index==length:
                lst.append(currentlist.copy())
                return
            
            currentlist.append(arr[index])
            sets(length,index+1,currentlist)
            currentlist.pop()
            sets(length,index+1,currentlist)
        
        sets(len(arr),0,currentlist)
        
        return lst
            