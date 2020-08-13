class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        # rotation logic: 
        # direction: N,E = 1,0: facing north. 0,1: facing East
        # R: turn right: new_x, new_y = -old_y, old_x
        # L: turn left:  new_x, new_y = old_y, -old_x
        
        # Uing pen and paper it is easy to notice that a cycle is formed only if the robot returns to origin or faces in any other direction than north at the end of one instruction cycle
        
        
        pos_n, pos_e = 0,0
        dir_n, dir_e = 1, 0
        
        for i in instructions: 
            if i == 'G':
                pos_n, pos_e = pos_n + dir_n, pos_e + dir_e
            elif i == 'R':
                dir_n, dir_e = -dir_e, dir_n
            else:
                dir_n, dir_e = dir_e, -dir_n
                
        if pos_n == 0 and pos_e == 0:
            return True
        
        if dir_n == 1 and dir_e == 0:
            # Facing North
            return False
        
        return True