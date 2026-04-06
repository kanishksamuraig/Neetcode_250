class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort();count=0
        l=0;r=len(people)-1
        while(l<=r):
            if people[l]+people[r]<=limit:
                count+=1
                l+=1
                r-=1
            elif people[r]<=limit:
                count+=1
                r-=1
            if r==l and people[r]<=limit:
                count+=1
                r-=1
        return count