class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        fact = [1]
        for i in range(rowIndex):
            x = fact[-1]
            fact.append(x*(i+1))
        res = []
        for k in range(rowIndex+1):
            x = fact[rowIndex]//(fact[k]*fact[rowIndex-k])
            res.append(x)
        
        return res