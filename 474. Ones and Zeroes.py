import functools

class Solution:
    
    count = 0
    
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        self.count = 0
        newStrs = []
        for s in strs:
            if len(s) == 1:
                if s == '0':
                    if m == 0:
                        continue
                    m -= 1
                else:
                    if n == 0:
                        continue
                    n -= 1
                self.count += 1
            else:
                newStrs.append(s)
                
        newStrs.sort(key = lambda x: len(x))
        self.helper(tuple(newStrs), 0, m, n, self.count)
        
        return self.count
        
        
    def getCount(self, s):
        o = s.count('1')
        z = s.count('0')
        return (z,o)


    @functools.lru_cache(maxsize=None)
    def helper(self, strs, idx, m, n, count):
        
        if idx >= len(strs) or len(strs[idx]) > m+n:
            self.count = max(count, self.count)
            return
        
        # Skip this one and go ahead
        self.helper(strs, idx+1, m, n, count)
        
        m_, n_ = self.getCount(strs[idx])
        # print(m_, n_)
        m, n = m-m_, n-n_
        
        if m >= 0 and n >= 0:
            # Add this one and go ahead
            self.helper(strs, idx+1, m, n, count+1)
            
        return




            