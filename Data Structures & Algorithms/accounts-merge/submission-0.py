class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    #find path compression
    def find(self,value):
        v = value
        if v!=self.parent[v]:
            v = self.find(self.parent[v])
        self.parent[value] = v
        return v
    def union(self,u,v):
        ultu = self.find(u)
        ultv = self.find(v)
        if ultu!= ultv:
            if self.rank[ultu]>=self.rank[ultv]:
                self.parent[ultv] = ultu
                if self.rank[ultu] == self.rank[ultv]:
                    self.rank[ultu]+=1
            else:
                self.parent[ultu] = ultv
            return False
        return True
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        accs = {index:account[1:] for index,account in enumerate(accounts)}
        emails = {}
        print(accs)
        for index in accs:
            for account in accs[index]:
                if account not in emails:
                    emails[account] = index
                else:
                    dsu.union(emails[account],index)
        dig={}
        for email in emails:
            ultu = dsu.find(emails[email])
            if ultu not in dig:
                dig[ultu] = []
            dig[ultu].append(email)
        lst=[]
        for i in range(len(accs)):
            if i not in dig:
                continue
            lst.append([accounts[i][0]]+sorted(dig[i]))
        return lst


        