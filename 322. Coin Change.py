import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def getOpt(i):
            if i<0:
                return 0
            else:
                return opt[i]
        
        l = len(coins)
        if not coins:
            return -1
        if amount == 0:
            return 0
        min_c = min(coins)
        if amount < min_c:
            return -1
        if l == 1:
            if amount%coins[0] == 0:
                return amount//coins[0]
            else:
                return -1
            
        opt = [0]
        coins.sort()
        for i in range(1,amount+1):
            # print(opt)
            temp = amount*2
            for c in coins:
                if c>i:
                    break
                else:
                    # print('here')
                    temp2 = opt[i-c]+1
                    temp = min(temp, temp2)
            
            opt.append(temp)
            
        # print(opt)
        if opt[-1] > amount:
            return -1
        
        return opt[-1]
        
            
            
            
            
            
            
            
            
            
        