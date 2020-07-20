class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret = str(secret)
        guess =  str(guess)
        
        bulls, cows = 0, 0 #correct and wrong locations
        s_counter = Counter(secret)
        g_counter = Counter(guess)
        
        
        for k in g_counter:
            if k in s_counter:
                cows += min(s_counter[k], g_counter[k])
                
        for x,y in zip(secret,guess):
            if x == y:
                bulls += 1
                cows -= 1
            
        return str(bulls)+'A'+str(cows)+'B'