from collections import OrderedDict
import heapq
from collections import deque
from math import inf

def getSkyline_fast(buildings):
    if not buildings: return []
    if len(buildings) == 1: return [[buildings[0][0],buildings[0][2]], [buildings[0][1], 0]]
    d_queue = deque()
    stack = []
    c_end = s_end = curr_ind = buildings[0][0]
    for building in buildings: s_end = max(s_end, building[1])
    result = {buildings[0][0]:[buildings[0][0],buildings[0][2]]}
    ind = 0
    l = len(buildings)
    while curr_ind <= s_end:
        while ind < l:
            b = buildings[ind]
            c_end = max(c_end, b[1])
            if b[0] > curr_ind:
                if not d_queue:
                    curr_ind = b[0]
                    break
                curr_ind+=1
                break
            if d_queue:
                while d_queue[0][1] <= curr_ind:

                    d_queue.popleft()
                    if d_queue and d_queue[0][0] < curr_ind:
                        result[curr_ind] = [curr_ind, d_queue[0][2]] 
                    else: 
                        result[curr_ind] = [curr_ind,0]
                    if not d_queue: break

            if not d_queue or b[2] > d_queue[0][2]:
                result[b[0]] = [b[0],b[2]]
                d_queue.appendleft(b)
            else:
                while d_queue[-1][2] < b[2] and d_queue[-1][0]:
                    stack.append(d_queue.pop())
                d_queue.append(b)
                while stack:
                    d_queue.append(stack.pop())

            ind+=1

        if d_queue:
            while d_queue[0][1] <= curr_ind:

                d_queue.popleft()
                if d_queue and d_queue[0][0] < curr_ind:
                    result[curr_ind] = [curr_ind, d_queue[0][2]] 
                else: 
                    result[curr_ind] = [curr_ind,0]
                if not d_queue: break
        if ind >= l: 
            curr_ind+=1
    prev_end = buildings[0][0]
    for b in buildings:
        if b[0] > prev_end:
            result[prev_end] = [prev_end, 0]
            if result.get(b[0], (0,0))[1] < b[2]:
                result[b[0]] = [b[0],b[2]]
        prev_end = max(b[1],prev_end)
    result = list(result.values())
    result.sort(key = lambda x: x[0])
    prev = 0
    l = len(result)
    i = 0
    while i < len(result):
        if result[i][1] == prev:
            del result[i]
        else:
            prev = result[i][1]
            i+=1
    return result

def getSkyline_slow(buildings):
    if not buildings: return []
    if len(buildings) == 1: return [[buildings[0][0],buildings[0][2]], [buildings[0][1], 0]]
    maxHeight = OrderedDict()
    prev_end = float("inf")
    skyline_end = buildings[0][0]
    result = []
    for building in buildings:
        begin, end, height = building
        if skyline_end < begin:
            maxHeight[prev_end+1] = 0
            maxHeight = list(maxHeight.items())
            result.append(list(maxHeight[0]))
            prev_height = result[-1][1]
            for pair in maxHeight[1:]:
                if pair[1] == prev_height:
                    continue
                else:
                    if pair[1] > prev_height:
                        result.append(list(pair))
                    else:
                        result.append([pair[0]-1,pair[1]])
                    prev_height = pair[1]
            del maxHeight
            maxHeight = OrderedDict()
        prev_end = end
        if end <= skyline_end and height < maxHeight[end]:
            continue
        for x in range(begin,end+1):
            maxHeight[x] = max(height, maxHeight.get(x,0))
        skyline_end = max(skyline_end,end)
    maxHeight[skyline_end+1] = 0
    maxHeight = list(maxHeight.items())
    if result: 
        prev_height = result[-1][1]
    else:
        prev_height = 0
    for pair in maxHeight[0:]:
        if pair[1] == prev_height:
            continue
        else:
            if pair[1] > prev_height:
                result.append(list(pair))
            else:
                result.append([pair[0]-1,pair[1]])
            prev_height = pair[1]
    return result      


buildings = [[2,4,70],[3,8,30],[6,100,41],[7,15,70],[10,30,102],[15,25,76],[60,80,91],[70,90,72],[85,120,59]]
#[[2,70],[4,30],[6,41],[7,70],[10,102],[30,41],[60,91],[80,72],[90,59],[120,0]]
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
#[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# buildings = [[0,2,3],[2,5,3]]

print(getSkyline_fast(buildings))
