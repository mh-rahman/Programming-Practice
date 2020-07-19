class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def helper(constructed,k,target,res):
            # print(constructed,k,target,res)
            if len(constructed) == k and target == 0:
                res.append(constructed.copy())
                return
            if len(constructed) == k or target == 0:
                return
            start = 1 if not constructed else constructed[-1]+1
            for i in range(start,min(target,9)+1):
                constructed.append(i)
                helper(constructed,k,target-i,res)
                constructed.pop()
            return
        
        res = []
        helper([],k,n,res)
        print(res)
        return res