class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res, fact = [], [1] #list of digits
        for i in range(n):
            fact.append((i+1)*fact[-1])
        k-=1
        num = [i+1 for i in range(n)]
        for idx in range(n):
            f = fact[n-idx-1]
            i = k//f
            # print('fact =',f,'num index =',i)
            res.append(num[i])
            del(num[i])
            idx, k = idx+1, k%f

        return ''.join([str(x) for x in res])
        