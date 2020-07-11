class Solution:
    
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(co,ind,nums,target):
            # print(co,ind)
            if sum(co) >= target or ind >= len(nums):
                if sum(co) == target:
                    # print('here',co)
                    co = '#'.join([str(x) for x in co])
                    res.add(co)
                return
            
            helper(co.copy(),ind+1,nums,target)
            co.append(nums[ind])
            helper(co.copy(),ind+1,nums,target)
            return
        
        
        res = set()
        nums.sort()
        helper([],0,nums,target)
        res = [s.split('#') for s in res]
        for i in range(len(res)):
            res[i] = [int(c) for c in res[i]]
            
        # print(res)
        
        return res
        
        
        
        
        
        
        
        
        
        
        
    
    def inProgresscombinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        nums = [x for x in nums if x <= target]
        nums.sort()
        
        nums_dict = {}
        for i,n in enumerate(nums):
            if n not in nums_dict:
                nums_dict[n] = i
        
        res1 = [[x] for x in nums_dict.keys()]
        
        
        
        
        for i in range(len(nums)):
            for comb in res1:
                if sum(comb) == target:
                    res.append(comb)
            res1 = [comb+[x] for comb in res1 for x in nums[nums_dict[comb[-1]]+1:] if x >= comb[0] and sum(comb)+x <= target]
            if not res1:
                break

        print(res1)
        print(res)
        return []
        