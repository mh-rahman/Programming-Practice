class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def getcolumn(x,y,m,direction): #direction = 1: down
            temp = []
            if direction<0:
                m = x-m+1
            else:
                m = x+m-1
            # print('getcol',x,y,m,direction)
            for i in range(x,m,direction):
                temp.append(matrix[i][y])
            # print(i+direction,y)
            return temp,i+direction,y
            
        def getrow(x,y,n,direction): #direction = 1: right
            temp = []
            if direction<0:
                n = y-n+1
            else:
                n = y+n-1
            # print('getrow',x,y,n,direction)
            j = y
            for j in range(y,n,direction):
                temp.append(matrix[x][j])
            # print()
            return temp,x,j+direction
        
        # print(matrix)
         
        m1 = m = len(matrix)
        if m1 == 0:
            return []
        n1 = n = len(matrix[0])
        res = []
        ind = 0
        while m>0 and n>0:
            x = y = ind
            # print(res)
            if m ==1 and n == 1:
                res = res+[matrix[x][y]]
                break
            if m == 1:
                # print('Here')
                temp,x,y = getrow(x,y,n,1)
                res = res+temp+[matrix[x][y]]
                break
            if n == 1:
                # print('Here2')
                temp,x,y = getcolumn(x,y,m,1)
                res = res+temp+[matrix[x][y]]
                break
            temp1,x,y = getrow(x,y,n,1)
            temp2,x,y = getcolumn(x,y,m,1)
            temp3,x,y = getrow(x,y,n,-1)
            temp4,x,y = getcolumn(x,y,m,-1)
            res = res+temp1+temp2+temp3+temp4
            ind+=1
            m-=2
            n-=2
            
        # print(res)
        return res
            