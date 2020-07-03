class Solution:
    def threeSum(self, nums):   
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length-2): #[8]
            if nums[i]>0: break #[7]
            if i>0 and nums[i]==nums[i-1]: continue #[1]
            l, r = i+1, length-1 #[2]
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total<0: #[3]
                    l+=1
                elif total>0: #[4]
                    r-=1
                else: #[5]
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l]==nums[l+1]: #[6]
                        l+=1
                    while l<r and nums[r]==nums[r-1]: #[6]
                        r-=1
                    l+=1
                    r-=1
        return res
    
    def myThreeSum(self, nums: List[int]) -> List[List[int]]:
        # length = len(nums)
        # if length < 3:
        #     return []
        # nums.sort()
        num_counter = Counter(nums)
        res = set()
        for x in num_counter:
            num_counter[x]-=1
            for y in num_counter:
                if num_counter[y] < 1:
                    continue
                num_counter[y]-=1
                z = -(x+y)
                temp = sorted([x,y,z])
                a1,a2,a3 = temp
                if num_counter.get(z,0) > 0:
                    res.add(str(a1)+'#'+str(a2)+'#'+str(a3))
                num_counter[y]+=1
            num_counter[x]+=1
            
        res = [x.split('#') for x in res]
        for i in range(len(res)):
            res[i] = [int(s) for s in res[i]]
            
        # print(res)
        
        return res