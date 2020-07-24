class Solution:
    def canPlaceFlowers(self, f: List[int], n: int) -> bool:
        if not n: return True
        if len(f) < 3:
            if 1 not in f and n < 2:
                return True
            else:
                return False
        
        if f[:2] == [0,0]:
            n -= 1
            f[0] = 1
        count = 0
        for i in range(len(f)):
            if f[i] == 1:
                n -= max(0,count//2 - (1-count%2))
                count = 0
                continue
            else:
                count += 1
            if n <= 0:
                return True
            # print(i,n)
        return False if n-count//2 > 0 else True