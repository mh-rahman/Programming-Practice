class Solution:
    def candy(self, ratings: List[int]) -> int:
        #Child with no lower rated neighbour gets 1 candy
        #Ex: 1,2,2 can have candies 1,2,1 respectively
        #Add 1 to left entries from "ones". For the last sub-array, also add to right
        
        l = len(ratings)
        res = [1]*l
        for i in range(1,l):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1]+1

        for i in range(l-1,0,-1):
            if ratings[i-1] > ratings[i]:
                res[i-1] = max(res[i-1],res[i]+1)

        return sum(res)