def cmax(nums,ci,cj):
    l=len(cmax)
    cl_sum=nums[ci]
    temp=cl_sum
    while cl_sum>=temp and ci>=0:
        temp=cl_sum
        ci-=1
        cl_sum+=nums[ci]
    ci+=1
    cl_sum=temp

    cr_sum=nums[cj]
    temp=cr_sum
    while cr_sum>=temp and cj<l:
        temp=cr_sum
        cj+=1
        cr_sum+=nums[cj]
    cj-=1
    cr_sum=temp

    c_sum=cl_sum+cr_sum


def recmax(nums):
        l=len(nums)
        print('nums = ',nums)
        if l==1:
            return nums[0]
        else:
            ci=l//2-1
            cj=l//2
            lMax=recmax(nums[0:cj])
            rMax=recmax(nums[cj:l])

            cMax=cmax(nums,ci,cj)

            if c_sum > l_sum and c_sum > r_sum:
                return c_sum
            elif r_sum > c_sum and r_sum > c_sum:
                return r_sum
            else:
                return l_sum


l=[-1,2,4,-2]
sum=recmax(l)
