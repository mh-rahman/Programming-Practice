class Solution:
    lookup = []
    def generate(self, n: int) -> List[List[int]]:
        if n <= len(self.lookup):
            return self.lookup[:n]
        
        if not self.lookup:
            self.lookup = [[1]]
        
        idx = len(self.lookup)
        while idx<n:
            temp = []
            prev = 0
            for x in self.lookup[-1]:
                temp.append(prev+x)
                prev = x
            temp.append(1)
            self.lookup.append(temp)
            
            idx+=1
            
        return self.lookup[:n]
            