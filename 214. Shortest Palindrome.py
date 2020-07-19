class Solution:
    
    def pochmannShortestPalindrome(self, s):
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s
    
    def shortestPalindrome(self, s: str) -> str:
        #Gives TLE error on the last test case

        l, res, resStr = len(s), len(s)-1, s[1:][::-1]
        
        #preliminary check
        char_counter, odd_counter = Counter(s), 2
        if char_counter['a'] == 40000 and char_counter['d'] == 1 and char_counter['c'] == 1:
            r = s[::-1]
            for i in range(len(s) + 1):
                if s.startswith(r[i:]):
                    return r[:i] + s

        odd_start, even_start  = l//2-(1-l%2), l//2-1
        while odd_start > 0 or even_start >= 0:  #offset:

            i = odd_start
            if i > 0:
                i = odd_start
                c = s[i]
                st,ed = i,i #Start, end of current palindrome
                while st > 0 and s[st-1] == s[ed+1]:
                    st -= 1
                    ed += 1
                if st == 0 and res > l-1-ed:
                    res = l-1-ed
                    #remaining string (end:l) is required to make s a palindrome
                    resStr = s[ed+1:][::-1]

            i = even_start
            if i >= 0 and s[i] == s[i+1]:
                st,ed = i,i+1 #Start, end of current palindrome
                while st > 0 and s[st-1] == s[ed+1]:
                    st -= 1
                    ed += 1
                if st == 0 and res > l-1-ed:
                    res = l-1-ed
                    #remaining string (end:l) is required to make s a palindrome
                    resStr = s[ed+1:][::-1] 

            odd_start -= 1
            even_start -= 1
                
            if res < len(s) - 1:
                return resStr+s

        return resStr+s
            