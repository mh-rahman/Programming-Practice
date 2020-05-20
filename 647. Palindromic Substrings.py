class Solution:
    def countSubstrings(self, s: str) -> int:
        
        l = len(s)
        if l<2:
            return l
        
        #get odd count (including unit length), even count
        odd_count = 0
        i = 0
        while i<l:
            j = 0
            while i+j<l and i-j>=0:
                if s[i+j] != s[i-j]:
                    break
                else:
                    odd_count+=1
                    j+=1
            i+=1
        
        #return odd_count + even_count
        even_count = 0
        i = 0
        while i<l-1:
            j = 0
            while i-j>=0 and i+j+1<l:
                a,b = s[i-j], s[i+j+1]
                if a!=b:
                    break
                else:
                    even_count+=1
                    j+=1
            i+=1
        
        return odd_count + even_count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        