class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #Sort. for each n find l,r such that sum gets closer to target
        #i.e. while l<r if sum<target l+=1 else r-=1
        #if l==i: l+=1 continue

        nums.sort()
        length = len(nums)
        diff,closest = math.inf,0
        for i in range(length):
            l,r = 0,length-1
            # print(i,'=',nums[i],l,'=',nums[l],r,'=',nums[r])
            while l < r:
                if l == i:
                    l+=1
                    continue
                if r == i:
                    r-=1
                    continue
                currsum = nums[i]+nums[l]+nums[r]
                # print('currsum =',currsum)
                if abs(currsum-target) < diff:
                    diff = abs(currsum-target)
                    closest = currsum
                if currsum < target:
                    l+=1
                    continue
                elif currsum > target:
                    r-=1
                    continue
                else:
                    return currsum

        return closest