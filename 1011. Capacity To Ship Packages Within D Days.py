class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        def isPossible(limit):
            curr = 0
            days = 1
            for w in weights:
                if curr+w > limit:
                    days+=1
                    curr = w
                    if days > D:
                        return False
                else:
                    curr+=w
            return True
        
        if len(weights) == 1:
            return weights[-1]
        
        maxlimit = max(weights)
        if isPossible(maxlimit):
            return maxlimit

        flag = True
        temp = 1
        limit = maxlimit + temp
        
        while flag:
            limit = maxlimit + temp
            if not isPossible(limit):
                temp*=2
            elif temp == 1:
                maxlimit = limit
                flag = False
            else:
                maxlimit = maxlimit + temp//2
                temp = 1
        
        return maxlimit