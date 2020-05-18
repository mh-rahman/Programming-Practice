class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = len(nums)
        sumDict = {0:1}
        count = 0
        currSum = 0
        for n in nums:
            currSum+=n
            count+=sumDict.get(currSum-k,0)
            sumDict[currSum] = sumDict.get(currSum,0)+1
            
        return count

        
        
        ###Matrix Approach - Does not leverage the fact that same sum can repeat multiple times because of negative numbers
        # l = len(nums)
        # res = [['a']*l for x in range(l)]
        # for i in range(l):
        #     res[i][i] = nums[i]
        # for diff in range(1,l):
        #     i = 0
        #     j = i+diff
        #     while j<l:
        #         res[i][j] = res[i+diff][j] + res[i][j-1]
        #         i+=1
        #         j+=1
        # count = 0
        # for i in range(l):
        #     count+=res[i][i:].count(k)
        # return count