class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        if n < 2:
            return s
        
        l = 0
        r = n-1
        
        while r > l:
            if s[l] != s[r]:
                s[l], s[r] = s[r], s[l]
            l+=1
            r-=1
            
        return s