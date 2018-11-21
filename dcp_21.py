inp = [(30,75), (0,50), (60,150)]

inp = sorted(inp)
rooms = 1
for i in range(1,len(inp)):
    if inp[i][0] >= inp[i-1][1]:
        rooms += 1

print(rooms)
