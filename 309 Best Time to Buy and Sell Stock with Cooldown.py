class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def getOpt(j):
            if j<0:
                return 0
            else:
                return opt[j]
        
        l = len(prices)
        if l <=1:
            return 0
        if l==2:
            return max(prices[1] - prices[0], 0)
        
        opt = [0]*l
        opt[1] = max(prices[1] - prices[0], 0)
        opt[2] = max(prices[2] - prices[0], prices[2] - prices[1], opt[1])
        for i in range(3,l):
            # temp = 0
            temp = opt[i-1]
            for j in range(i):
                temp = max(temp, prices[i] - prices[j] + getOpt(j-2))
            
            opt[i] = temp
        # print(opt)

#         opt = [0]*(l+2)
#         # opt[1] = max(prices[1] - prices[0], 0)
#         # opt[2] = max(prices[2] - prices[0], prices[2] - prices[1], 0)
#         for i in range(l):
#             # temp = 0
#             temp = opt[i+1]
#             for j in range(2,i+2):
#                 temp = max(temp, prices[i] - prices[j] + opt[j])
            
#             opt[i+2] = temp
#         print(opt)
        
        
        
        return opt[-1]