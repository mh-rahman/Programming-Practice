from fractions import Fraction
from math import gcd
from functools import reduce


def printMatrix(matrix,s='Matrix'):
    print(s)
    print('[')
    for row in matrix:
        print('[',end = ' ')
        for n in row:
            print(str(n),end=',\t')
        print(']',)
    print(']')


def copyMatrix(matrix):
    return [[n for n in row] for row in matrix]


def getAbsorptionStates(matrix):
    isRegular = [1]*len(matrix)
    for i,row in enumerate(matrix):
        if sum(row) == 0:
            isRegular[i] = 0
    return isRegular


def getStandardForm(matrix, newOrder):
    #Returns standard form of transition matrix
    transitionMatrix = [[n for n in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            oldi, oldj = newOrder[i], newOrder[j]
            transitionMatrix[i][j] = matrix[oldi][oldj]
    return transitionMatrix


def getProbForm(matrix):
    res = copyMatrix(matrix)
    for i in range(len(res)):
        s = sum(res[i])
        if not s:
            continue
        for j in range(len(res[0])):
            # temp = str(res[i][j])+'/'+str(s)
            # res[i][j] = Fraction(temp)
            res[i][j] = Fraction(res[i][j], s)
    return res


def matMul(A,B):
    assert (len(A[0]) == len(B)), "Matrix Multiplication Error: Dimensions invalid"
    res = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(res)):
        for j in range(len(res[0])):
            res[i][j] = sum([x*y for x,y in zip(A[i], [B[k][j] for k in range(len(B))])])
    return res


def getInverse(A):
    ##Using row operation method i.e. Gaussian Jordan elimination method
    ##Using fractions to make life easier via automatic reductions and no approximations

    ##Add Identity  matrix to the right of A
    res = copyMatrix(A)
    n = len(A)
    for i in range(n):
        res[i] = A[i] + [0 if j != i else 1 for j in range(n) ]

    #Selecting a pivot element
    for k in range(n):
        pivot = res[k][k]
        if pivot == 0:
            #Avoiding divide-by-zero error
            continue

        #Make pivot 1 i.e. divide row i with pivot
        # for j in range(2*n):
        for j in range(k,2*n):
            res[k][j] = res[k][j]/pivot

        '''
        Make other values in column i equal to zero
        res[i][j] = res[i][j] - res[i][k]*res[k][j] for all i != k for all j in range [k,n]
        This will make all row[i][k] == 0 i.e. column k will become zero
        '''
        for i in range(n):
            factor = res[i][k]
            if i == k or factor == 0:
                continue
            for j in range(k,2*n):
                res[i][j] = res[i][j] - res[k][j]*factor
    
    #return the second half of res
    for i in range(n):
        res[i] = res[i][n:]

    return res



def solution(matrix):

    ##Check which states are absorption states vs regular
    isRegular = getAbsorptionStates(matrix)
    if isRegular[0] == 0:
        res = [0]*len(matrix)
        res.append(1)
        res[0] = 1
        return res


    ##Get number of absorption states
    noAbsorptionStates = len(isRegular)-sum(isRegular)
    if noAbsorptionStates == len(matrix):
        print('Here')
        return [1,1]

    ##Calculate new order for transition matrix
    order = [(isRegular[i],i) for i in range(len(matrix))]
    # print('Old =', order)
    newOrder = [y for x,y in sorted(order)]
    # print('New =', newOrder)

    #Get standard form of transition matrix
    transitionMatrix = getStandardForm(matrix, newOrder)
    # printMatrix(transitionMatrix, 'Transition Matrix =')

    #Reduce to probability form - using fractions
    transitionMatrix = getProbForm(transitionMatrix)
    # printMatrix(transitionMatrix, 'Prob form of transition matrix =')

    #Splitting standard form into its components i.e. I, Z, Q, R (in clockwise direction)
    #R = [[n for n in row[:noAbsorptionStates]] for row in transitionMatrix[noAbsorptionStates:]]
    R = [[n for n in row[:noAbsorptionStates]] for row in transitionMatrix[noAbsorptionStates:]]
    Q = [[n for n in row[noAbsorptionStates:]] for row in transitionMatrix[noAbsorptionStates:]]

    #F_ = I-Q
    F_ = [[-n for n in row] for row in Q]
    for i in range(len(F_)):
        F_[i][i] += 1

    # printMatrix(Q, 'Q =')
    # printMatrix(R, 'R =')
    # printMatrix(F_, 'F_ =')

    #F = (I - Q)**-1
    F = getInverse(F_)
    printMatrix(F, 'After Inverse, F =')
    

    limitingMatrix = matMul(F,R)
    printMatrix(limitingMatrix, 'limitingMatrix =')

    ##Get Denominators
    denominators = [x.denominator for x in limitingMatrix[0] if type(x) == Fraction]
    # print('Denominators: ', denominators)

    #Get LCM of denominators
    lcm = reduce(lambda a,b: a*b // gcd(a,b), denominators)
    # print(lcm)

    #Get res by multiplying the numerators with lcm/x.denominator
    res = [x.numerator*(lcm/x.denominator) for x in limitingMatrix[0]]
    res.append(lcm)
    
    return res


    # res  = limitingMatrix[0][:noAbsorptionStates] + [denominator]
    # printMatrix(res, 'Res =')


# matrix = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
# iden = [[1,0,0],[0,1,0],[0,0,1]]
# matrix = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
matrix = [[0, 0, 0, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
# matrix = [[0]]
print(solution(matrix))
# printMatrix(getInverse(iden), 'Testing Inverse:')
# printMatrix(getProbForm(matrix), 'Test =')

# a = Fraction(-4,-3)
# print(type(a) == Fraction)