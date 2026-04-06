class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort();l=0;r=len(nums)-1;hashmap={};lst=[];hashset=set()
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                if -(nums[i]+nums[j]) in hashmap:
                    x=-(nums[i]+nums[j])
                    if i!=hashmap[x] and j!=hashmap[x] and tuple(sorted([nums[i],nums[j],x])) not in hashset:
                        lst.append([nums[i],nums[j],x])
                        hashset.add(tuple(sorted([nums[i],nums[j],x])))
        return lst


