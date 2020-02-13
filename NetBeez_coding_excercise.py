def func(a,x,y,moves):
    for move in moves:
        if move == "L":
            y = (y-1)%(a)
        elif move == "R":
            y = (y+1)%(a)
        elif move == "U":
            if x-1>=0:
                x = x-1
        elif move == "D":
            if x+1<=a:
                x = x+1
        print(move, x, y)
    return [x,y]


# print(func(3, 0, 0,"RDD"))
# print(func(3, 1, 0, "LLUU"))