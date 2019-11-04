n=int(input("Enter number of items: "))
print("Enter {} weight: ".format(n))
#length=[2,4,4,6]
length=[]
for i in range(0,n):
    length.append(int(input()))
print("Enter {} values: ".format(n))
weight=[]
for i in range(0,n):
    weight.append(int(input()))
#weight=[1,4,6,3]
m=int(input("Max weight: "))

# length=[2,4,4,6]
# weight=[1,4,6,3]
# m=8


opt = [[0] * (m+1) for i in range(n+1)]

# print(opt)
for i in range(0,n+1):
    for j in range (0,m+1):
        if i==0 or j==0:
            opt[i][j]=0
            # print('i=',i,'j=',j)
            # print(opt[0])
        elif j>=length[i-1]:
            # print('i=',i,'j=',j)
            opt[i][j]=max(opt[i-1][j],weight[i-1]+opt[i-1][j-length[i-1]])
            # print(opt[0])
            # print(opt[i])
        else:
            # print('i=',i,'j=',j)
            opt[i][j]=opt[i-1][j]
            # print(opt[0])

# print(length)
print(opt)

print(opt[n][m])
