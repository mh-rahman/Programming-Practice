class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxC = 0
        start = 0
        end = len(height) - 1
        
        while start < end:
            capacity = (end - start)*min(height[end], height[start])
            if height[end] >= height[start]:
                start+=1
            else:
                end-=1
                
            maxC = max(maxC, capacity)
            
        return maxC