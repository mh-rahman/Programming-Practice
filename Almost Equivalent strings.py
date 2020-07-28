from collections import Counter

s = ['aabaab','aaaaabb']
t = ['bbabbc','abb']
res = []
for S,T in zip(s,t):
    if len(S) != len(T):
        res.append('NO')
        continue
    s_counter = Counter(S)
    t_counter = Counter(T)
    temp = 'Yes'
    for k in s_counter:
        if abs(s_counter[k] - t_counter.get(k,0)) > 3:
            temp = 'No'
            break
    res.append(temp)

print(res)