class Solution:
    lookup = [2]
    def countPrimes(self, n: int) -> int:
        def isPrime(i):
            idx = 0
            sqt = sqrt(i)
            # print(sqt)
            while idx < len(self.lookup) and self.lookup[idx] <= sqt:
                if i%self.lookup[idx] == 0:
                    return False
                idx+=1
            return True
        
        if n > self.lookup[-1]:    
            start = self.lookup[-1]
            for i in range(start+1,n+1):
                if isPrime(i):
                    self.lookup.append(i)
            # print(self.lookup)
            return len(self.lookup) if n != self.lookup[-1] else len(self.lookup)-1
            
        idx = 0
        while idx<len(self.lookup) and self.lookup[idx] < n:
            idx+=1
        # print(self.lookup)
        return idx    
        