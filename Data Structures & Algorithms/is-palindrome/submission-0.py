class Solution:
    def isPalindrome(self, s: str) -> bool:

        left=0
        right=len(s)-1
        while(left<=right):
            print(s[right],s[left])
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[right].lower()!=s[left].lower():
                return False
            right-=1
            left+=1
        return True