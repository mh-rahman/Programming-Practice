class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l = len(nums)
        if l < 3:
            return False
        
        res = [None]*l
        
        for i in range(l)[::-1]:
            flag = True
            j = i+1
            limit = l
            while flag and j<limit:
                if nums[j]>nums[i]:
                    ## check entry at j and return true if exists
                    ## else add entry for i
                    if res[j]:
                        return True
                    else:
                        res[i] = nums[j]
                        j+=1
                    
                elif nums[j]<nums[i]:
                    ## check entry and if entry bigger than nums[i], copy
                    ## else increase j, set new limit
                    if not res[j]:
                        j+=1
                    else:
                        if res[j] > nums[i]:
                            res[i] = res[j]
                    break                
                else:
                    ##copy entry, dont do anything
                    res[i] = res[j]
                    break
                
        print(res)
        return False
            