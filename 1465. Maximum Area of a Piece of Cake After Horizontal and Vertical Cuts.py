class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        horiz = [horizontalCuts[0]]
        horiz+=[horizontalCuts[i] - horizontalCuts[i-1] for i in range(1,len(horizontalCuts))]
        horiz.append(h-horizontalCuts[-1])
        

        verticalCuts.sort()
        vert = [verticalCuts[0]]
        vert+=[verticalCuts[i] - verticalCuts[i-1] for i in range(1,len(verticalCuts))]
        vert.append(w-verticalCuts[-1])
            
        print(horiz)
        print(vert)
        return (max(horiz)*max(vert))%(10**9 + 7)