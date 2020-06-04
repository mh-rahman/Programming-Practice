class Solution:
    def trap(self, height: List[int]) -> int:
        #convert to list of tuples [(h,w) ]
        def getNewHeights(height):
            count = height[0][1] 
            prev = height[0][0]
            n_h = []
            for h,c in height[1:]:
                if h == prev:
                    count+=c
                else:
                    n_h.append([prev,count])
                    count = c
                    prev = h
            n_h.append([prev,count])
            return n_h
        
        def reduceHeights(n_h):
            i = 1
            water = 0
            while i < len(n_h)-1:
                p,c,n = n_h[i-1][0], n_h[i][0], n_h[i+1][0]
                if c < p and c < n:
                    n_h[i][0] = min(p,n)
                    water+=((n_h[i][0] - c)*n_h[i][1])
                i+=1

            n_h = getNewHeights(n_h)
            return n_h,water
        
        height = [[h,1] for h in height]
        l = len(height)
        if l < 2:
            return 0
        n_h = getNewHeights(height)
        water = 0
        new_water = 1
        while len(n_h) > 2 and new_water:
            n_h,new_water = reduceHeights(n_h)
            water+=new_water

        return water