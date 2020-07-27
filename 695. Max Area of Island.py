class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0:
                    continue
                area = 1
                st = [(x,y)]
                grid[x][y] = 0
                while st:
                    x,y = st.pop()
                    # print('Current = ({},{}). Next:'.format(x,y), end=' ')
                    for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                            # print('({},{})'.format(i,j), end = ', ')
                            grid[i][j] = 0
                            area += 1
                            st.append((i,j))
                    # print('')
                # print('Area from ({},{}) is {}.'.format(x,y,area))
                maxArea = max(maxArea,area)
        return maxArea