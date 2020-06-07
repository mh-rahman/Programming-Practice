class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c for c in s if c.isalnum()]
        i = 0
        while i < len(s):
            if s[i].isalpha():
                s[i] = s[i].lower()
            i+=1
        l = 0
        r = len(s) - 1
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        
        return True