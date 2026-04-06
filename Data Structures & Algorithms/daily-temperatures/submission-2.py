class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force
        stack=[]
        for index,num in enumerate(temperatures):
            j=index+1
            while(j<len(temperatures) and temperatures[j]<=num):
                j+=1
            if j==len(temperatures):
                stack.append(0)
                continue
            stack.append(j-index)
        return stack


