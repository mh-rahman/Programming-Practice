# nums = [7,4,7]
nums = [1,2,3]
l = len(nums)
t = 0
res = 0
lu = 0
for i,n in enumerate(nums):
    lu += n
    if n <= t:
        continue
    x = n - t
    res += x*(l-i)
    t += x

print(res+lu)
