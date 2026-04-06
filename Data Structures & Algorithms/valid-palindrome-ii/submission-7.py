class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s)<=2:
            return True
        l=0;r=len(s)-1;count=0
        while(l<=r):
            if s[l]!=s[r]:
                if s[l]==s[r-1] and s[l+1]==s[r] and count<1 and r-l!=1:
                    if s[l+1]==s[r-2]:
                        r-=1
                    elif s[l+2]==s[r-1]:
                        l+=1

                elif s[l]==s[r-1] and count<1:
                    r-=1
                elif s[l+1]==s[r] and count<1:
                    l+=1
                else:
                    return False
                count+=1
                continue
            l+=1
            r-=1
        return True

            