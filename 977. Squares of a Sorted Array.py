class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ind, res = bisect.bisect_left(A,0), []
        n,p= ind-1, ind
        if ind < len(A) and A[ind] == 0:
            res.append(0)
            p = ind+1
        
        while n >= 0 and p < len(A):
            if abs(A[n]) < abs(A[p]):
                res.append(A[n]*A[n])
                n -= 1
            else:
                res.append(A[p]*A[p])
                p += 1
                
        while n >= 0:
            res.append(A[n]*A[n])
            n -= 1
        
        while p < len(A):
            res.append(A[p]*A[p])
            p += 1
    
        return res