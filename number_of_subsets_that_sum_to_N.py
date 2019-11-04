def printSubsets(index,currentSum,pList):
    if index==1 and currentSum!=0 and optArray[currentSum][index]!=0:
        print("in if - 1")
        pList.append(array[index-1])
        print(pList)
        return
    if currentSum==0:
        print("in if - 2")
        print(pList)
        return
    if optArray[currentSum][index-1]!=0:
        print("in if - 3")
        newList=pList
        printSubsets(index-1,currentSum,newList)
    if currentSum>array[index-1] and optArray[currentSum-array[index-1]]!=0:
        print("in if - 4")
        pList.append(array[index-1])
        printSubsets(index-1,currentSum-array[index-1],pList)



arrayLength=int(input("Enter the size of array:"))
print("Enter ",arrayLength," numbers:")
array=[int(input()) for _ in range (0,arrayLength)]
sum=int(input("Enter the value of the sum:"))
optArray=[[0 for x in range (arrayLength+1)] for y in range (0,sum+1)]
for x in range (0,sum+1):
    for y in range (0,arrayLength+1):
        if x==0:
            optArray[x][y]=1
        elif y==0:
            optArray[x][y]=0
        else:
            if x<array[y-1]:
                optArray[x][y]=optArray[x][y-1]
            else:
                optArray[x][y]=optArray[x][y-1]+optArray[x-array[y-1]][y-1]

print(optArray)
print("Number of solutions= ",optArray[sum][arrayLength])
print(optArray[3][4])
#if optArray[sum][arrayLength]==0:
#    print("Given sum is not acheivable using the elsments of given array.")
#else:
#    printSubsets(arrayLength,sum,[])
