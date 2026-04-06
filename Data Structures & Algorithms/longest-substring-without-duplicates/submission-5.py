class Solution:
    def lengthOfLongestSubstring(self, arr: str) -> int:
        hash=set()
        left=0;right=0
        maximum=0
        while right<len(arr):
            
            if arr[right] in hash:
                hash.remove(arr[left])
                left+=1
            
            if arr[right] not in hash:
                hash.add(arr[right])
                maximum=max(maximum,right-left+1)
                right+=1
        return maximum