class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        if not n: return 0
        i,Q,sqrs,seen = 1,deque([]),[],set() #[num,count]
        while i**2 <= n:
            Q.append([i**2,1])
            sqrs.append(i**2)
            i+=1
        if sqrs[-1] == n: return 1
        while Q:
            # print(Q)
            num,count = Q.popleft()
            seen.add(num)
            for s in sqrs:
                if num+s == n:
                    res = count+1
                    return res
                if num+s > n:
                    break
                if num+s not in seen:
                    Q.append([num+s,count+1])
            
        return res

#         dp = self._dp
#         while len(dp) <= n:
#             dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
#         return dp[n]
    