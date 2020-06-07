class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        b = -1
        # s = 0
        i = 0
        while i < len(prices)-1:
            c,n = prices[i],prices[i+1]
            if b<0 and n>c:
                b = c
            elif b>=0 and b<c and n<c:
                profit+=(c-b)
                b = -1
            # print(c,n,b,profit)
            i+=1
            
        if b != -1:
            # print('hi',b,prices[-1]-b)
            profit+=max(0,prices[-1]-b)
            
        return profit