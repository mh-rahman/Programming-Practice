def solution(n: str):
    '''
    Probably BitMapnipulation..
    '''
    res, n = 0, int(n)
    while n > 1:
        res += 1
        if n%2 == 0:
            n = n >> 1
        elif n%4 == 1 or n == 3:
            n -= 1
        else:
            n += 1
    return res

    # return backtracker(int(n),{},2*int(n))



def backtracker(n,lookup,limit):
    # print(n)
    if n >= limit:
        return math.inf
    if n == 1:
        return 0
    if n in lookup:
        return lookup[n] if lookup[n] > 0 else math.inf
    # bfsQ = collections.deque([])
    
    lookup[n] = -1
    resMinus  = backtracker(n-1,lookup,limit) + 1
    # resPlus = backtracker(n+1,lookup,moves+1,limit)
    # res = min(resMinus, resPlus)
    res = resMinus
    if n%2 == 0:
        res = min(res, backtracker(n//2,lookup,limit)) + 1
    lookup[n] = res
    if n == 21:
        print(lookup)
    return res


print('res =',solution('15'))