class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def possiblecomb(string,turn):
            lst = []
            stri=list(string)
            for i in range(len(string)):
                original = stri[i]
                stri[i] = str((int(stri[i])+1)%10)
                lst.append(("".join(stri),turn))
                stri[i] = original
                stri[i] = str((int(stri[i])-1)%10)
                lst.append(("".join(stri),turn))
                stri[i] = original
            return lst
        
        queue = deque()
        queue.append(("0000",0))
        hash=set()
        for i in deadends:
            hash.add(i)
        if "0000" in hash:
            return -1
        finesse = set()

        while queue:
            string,turns = queue.popleft()
            if string==target:
                return turns
            turns+=1
            lst = possiblecomb(string,turns)
            for i in lst:
                if i[0] not in hash and i[0] not in finesse:
                    queue.append(i)
                    finesse.add(i[0])
        return -1
                

        