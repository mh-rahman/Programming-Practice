class Solution:
    def calculateMinimumHP(self, d: List[List[int]]) -> int:
        
        ##DP approach
        row, col = len(d), len(d[0])
        prev = 1
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                if i < row-1 and j < col-1:
                    prev = min(d[i][j+1], d[i+1][j])
                elif i < row-1:
                    prev = d[i+1][j]
                elif j < col-1:
                    prev = d[i][j+1]
                d[i][j] = max(1,prev-d[i][j])
                
        print(d)
        
        ##Greedy - 36/45
        while False:
#             row, col = len(d), len(d[0])
#             req = [[[0,0] for c in range(col)] for r in range(row)] #curr_h, req_h
#             # print(req)

#             curr = d[0][0]
#             req[0][0][1] = max(0, 1-curr)
#             req[0][0][0] = max(curr,1)
#             print(req[0][0])

#             for j in range(1,col):
#                 curr = d[0][j]
#                 incoming_health, incoming_req = req[0][j-1]
#                 curr_required = incoming_req + max(0, 1-(curr+incoming_health))
#                 curr_health = max(incoming_health+curr,1)
#                 req[0][j][0], req[0][j][1] = curr_health, curr_required

#             for i in range(1,row): 
#                 curr = d[i][0]
#                 incoming_health, incoming_req = req[i-1][0]
#                 curr_required = incoming_req + max(0, 1-(curr+incoming_health))
#                 curr_health = max(incoming_health+curr,1)
#                 req[i][0][0], req[i][0][1] = curr_health, curr_required

#             for i in range(1,row):
#                 for j in range(1,col):
#                     curr = d[i][j]
#                     incoming_health_l, incoming_req_l = req[i][j-1]
#                     incoming_health_t, incoming_req_t = req[i-1][j]
#                     required_l, required_t = incoming_req_l + max(0, 1-(curr+incoming_health_l)), incoming_req_t + max(0, 1-(curr+incoming_health_t))
#                     if required_l < required_t:
#                         curr_required = required_l
#                         curr_health = max(incoming_health_l+curr,1)
#                     else:
#                         curr_required = required_t
#                         curr_health = max(incoming_health_t+curr,1)
#                     req[i][j][0], req[i][j][1] = curr_health, curr_required


#             print(req)
#             print(req[-1][-1][-1])
#             return max(1,req[-1][-1][-1])
            pass
        
        return d[0][0]
        return d[0][0]