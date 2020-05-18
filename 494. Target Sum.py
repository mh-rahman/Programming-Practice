class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if len(nums) == 0:
            return 0
        
        # Brute Force Approach
#         def helper(start, end,target):
#             if start-end == 0:
#                 if target == 0:
#                     return 1
#                 return 0
#             count = helper(start+1,end,target+nums[start]) + helper(start+1,end,target-nums[start])
            
#             return count
#         # print(len(nums))
#         return helper(0,len(nums),S)

        ### Better Approach
        # sums = []
        # i = len(nums) - 1
        # sums = [nums[i],-nums[i]]
        # print(i,sums)
        # i-=1
        # while i>=0:
        #     print(i,sums)
        #     x = nums[i]
        #     temp_1 = [s+x for s in sums]
        #     temp_2 = [s-x for s in sums]
        #     sums = temp_1+temp_2
        #     del(temp_1,temp_2)
        #     i-=1
        # print(i,sums)
        # count = 0
        # for s in sums:
        #     if s == S:
        #         count+=1
        # return count
        
        ## Best Approach
        i = len(nums) - 1
        sum_dict = {}
        sum_dict[nums[i]] = sum_dict.get(nums[i],0)+1
        sum_dict[-nums[i]] = sum_dict.get(-nums[i],0)+1
        i-=1
        while i>=0:
            print(i,sum_dict)
            x = nums[i]
            new_dict = {}
            for s in sum_dict.keys():
                x1 = s+x
                x2 = s-x
                new_dict[x1] = new_dict.get(x1,0)+sum_dict[s]
                new_dict[x2] = new_dict.get(x2,0)+sum_dict[s]
            sum_dict = new_dict
            del(new_dict)
            i-=1
                                                           
            
        print(sum_dict)
        
        return sum_dict.get(S,0)
            
            
            
            
            
            
            
            
            
        