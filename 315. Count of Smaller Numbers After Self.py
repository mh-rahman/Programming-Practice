class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = [[n,i,0,0] for i,n in enumerate(nums) ]
        #val,index,pos,count
        
        def helper(nums):
            l = len(nums)
            if l < 2:
                return nums
            mid = l//2
            left = helper(nums[:mid])
            right = helper(nums[mid:])
            return merge(left,right)
        
        def merge(left,right):
            merged = []
            ll = len(left)
            lr = len(right)
            li = ri = mi = 0
            while li < ll and ri < lr:
                l = left[li]
                r = right[ri]
                if l < r:
                    val,ind,pos,count = l
                    count += max(0,mi-pos)
                    merged.append([val,ind,mi,count])
                    li+=1
                else:
                    val,ind,pos,count = r
                    count += max(0,mi-ll-pos)
                    merged.append([val,ind,mi,count])
                    ri+=1
                mi+=1
                
            while li < ll:
                l = left[li]
                val,ind,pos,count = l
                count += max(0,mi-pos)
                merged.append([val,ind,mi,count])
                li+=1
                mi+=1
                
            while ri < lr:
                r = right[ri]
                val,ind,pos,count = r
                count += max(0,mi-ll-pos)
                merged.append([val,ind,mi,count])
                ri+=1
                mi+=1
            return merged
        
        if not nums:
            return nums
        res = helper(nums)
        res.sort(key = lambda x: x[1])
        res = [x[3] for x in res]
        return res