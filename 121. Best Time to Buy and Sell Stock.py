class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        b = math.inf
        profit = -math.inf
        for p in prices:
            if p < b:
                b = p
            profit = max(profit,p-b)
        return profit
        
    def maxProfit2(self, prices: List[int]) -> int:
        profit = 0
        b = 0
        # s = 0
        i = 0
        while i < len(prices)-1:
            c,n = prices[i],prices[i+1]
            if not b and n>c:
                b = c
            elif b and b<c and n<c:
                profit+=(c-b)
                b = 0
            print(c,n,b,profit)
            i+=1
            
        if b:
            profit+max(0,prices[-1]-b)
            
        return profit