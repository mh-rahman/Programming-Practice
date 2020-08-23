#!/bin/python3

import math
import os
import random
import re
import sys

def findBeforeMatrix(after):
    
    if not after:
        return None
    
    m, n = len(after), len(after[0])
    before = [[0]*n for i in range(m)]

    for i in range(m):
        for j in range(n):
            before[i][j] = getAfterVal(after, i, j) - getAfterVal(after, i-1, j) - getAfterVal(after, i, j-1) + getAfterVal(after, i-1, j-1)

    return before

def getAfterVal(after, i, j):
    m, n = len(after), len(after[0])
    if 0 <= i < m and 0 <= j < n:
        return after[i][j]
    else:
        return 0
    
if __name__ == '__main__':