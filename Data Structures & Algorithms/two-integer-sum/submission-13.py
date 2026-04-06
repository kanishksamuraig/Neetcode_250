class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for index,num in enumerate(nums):
            if target-num in dict1:
                return [dict1[target-num],index]
            dict1[num]=index