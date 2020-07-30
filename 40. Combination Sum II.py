class Solution:
    
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        
        '''
        1. sort - [1,2,2,2,5], target = 7
        2. consider a number or don't
        3. If there are repeats, then:
            a. Consider:    Add it to constructed and move along as usual
            b. Don't:       For skipping, skip all
            
            This way all possible combinations will be taken care
        
        '''
        
        def helper(nums, target, ind, constructed, constructedSum, res):
            if target == 0:
                # Reached target. No need to explore further
                res.append(constructed.copy())
                return 
            
            if ind >= len(nums):
                return
            # print('curr = ({}, {}), target = {}, constructed = {}, constructedSum = {}'.format(ind, nums[ind],target,constructed,constructedSum))
            
            
            if nums[ind] > target:
                # We have overshot and no need to progress further
                # print('Overshot', constructed, nums[ind])
                return
            
            # Add it to constructed
            constructed.append(nums[ind])
            constructedSum += nums[ind]
            # print('Adding', nums[ind])
            helper(nums, target - nums[ind], ind+1, constructed, constructedSum, res)
            constructed.pop()
            constructedSum -= nums[ind]
            
            # Skipping duplicates
            temp = nums[ind]
            while ind < len(nums) and nums[ind] == temp:
                ind += 1
            
            # print('Skipping', temp)
            helper(nums, target, ind, constructed, constructedSum, res)
            
            return
        
        
        res = []
        nums.sort()
        helper(nums, target, 0, [], 0, res)
        
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def strignHashingCombinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
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
        