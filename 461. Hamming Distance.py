class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        dist = 0
        while x or y:
            # print(x,y)
            if x%2 != y%2:
                dist+=1
            x = x>>1
            y = y>>1
        return dist