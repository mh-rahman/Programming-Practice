#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the biggerIsGreater function below.
def swap (w,i,j):
    l=list(w)
    temp=l[j]
    l[j]=l[i]
    l[i]=temp
    return(''.join(l))


def biggerIsGreater(w):
    length=len(w)
    i=length-1
    if i==0:
        return "no answer"
    while w[i-1]<=w[i] and i>0:
        if i==1:
            return "no answer"
        i-=1
    
    if i==len(w)-1:
        return swap(w,i,i-1)
    suffixStart=i
    pivot=w[i-1]
    smallestInSuffix=i
    for i in range(suffixStart, length):
        if w[i]>=w[smallestInSuffix] and w[i]<pivot:
            smallestInSuffix=i
    newString=swap(w,suffixStart-1,smallestInSuffix)
    prefix=''.join(list(newString)[:suffixStart])
    print ("String is ",w,". newString is ",newString,". Prefix is ", prefix)
    newSuffixList=list(newString)[suffixStart:]
    #[suffixStart:].reverse()
    newSuffixList.reverse()
    suffix=''.join(newSuffixList)
    return prefix+suffix

    

    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
