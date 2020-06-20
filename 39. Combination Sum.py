class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def helper(constructed,idx,t):
            if t == 0:
                res.append(constructed)
                # print(idx,constructed)
                return
            if idx < 0 or t < candidates[idx]: #less than min
                return

            num = candidates[idx]
            mul = 0
            while t >= num*mul:
                temp = num*mul
                helper(constructed+[num]*mul,idx-1,t-num*mul)
                mul+=1            
            return
        
        res = []
        candidates.sort(reverse = True)
        helper([],len(candidates)-1,target)
        # print(res)
        return res