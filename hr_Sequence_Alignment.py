#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the commonChild function below. 
def mc(x,y): # Mismatch cost
    if x==y:
        return 0
    else:
        # global count
        # count+=1
        # print(x,y,count)
        return 50

# Linear space sequence alignment - score calculator:
# def commonChild(s1, s2):
#     #count=0
#     gp=2 #gap penalty
#     opt=[[gp*_y*(1-_x) for _x in range(2)] for _y in range(len(s1)+1)]
#     level=1
#     #print(opt)
#     for j in range(1,len(s2)+1):
#         opt[0][1]=j*gp
#         for i in range(1,len(s1)+1):
#             #print('i={}'.format(i))
#             opt[i][1]=min(mc(s1[i-1],s2[j-1])+opt[i-1][0],gp+opt[i-1][1],gp+opt[i][0])
#             # if(opt[i][1]==gp+opt[i-1][1] or opt[i][1]==gp+opt[i-1][0]):
#             #     count+=1
#         print(opt)
#         for i in range(1,len(s1)+1):
#             opt[i][0]=opt[i][1]
        
#     print('count={}'.format(count))
#     print(opt[len(s1)][1])
#     return count

def commonChild(s1, s2):
    gp=2 #gap penalty
    length_s1=len(s1)
    length_s2=len(s2)
    opt=[[0 for _x in range(length_s2+1)] for _y in range(length_s1+1)]
    for j in range(1,length_s2+1):
        opt[0][j]=j*gp
    for j in range(1,length_s1+1):
        opt[j][0]=j*gp
    
    for j in range(1,len(s2)+1):
        for i in range(1,len(s1)+1):
            mc = 0 if s1[i-1]==s2[j-1] else 50
            opt[i][j]=min(mc+opt[i-1][j-1],gp+opt[i-1][j],gp+opt[i][j-1])

        
    (i,j)=(length_s1,length_s2)
    count=0
    while (i,j)!=(0,0) and i>0 and j>0:
        if opt[i][j]==opt[i-1][j-1] and opt[i-1][j-1]<opt[i][j-1] and opt[i-1][j-1]<opt[i-1][j]:
            count+=1
            (i,j)=(i-1,j-1)
        elif opt[i][j-1] < opt[i-1][j]:
            (i,j)=(i,j-1)
        else:
            (i,j)=(i-1,j)

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
