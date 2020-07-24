def solution(s):
    # Your code here
    salutes, rightCounter = 0, 0
    for c in s:
        if c == '>':
            rightCounter += 1
        elif c == '<':
            salutes += (rightCounter*2)
    
    return salutes

print(solution(">----<"))
print(solution("<<>><"))
print(solution("--->-><-><-->-"))
