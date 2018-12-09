def pow(x,y):
    print(x,y)
    if y == 0:
        return 1
    if y == 1:
        return x
    if y % 2 == 0:
        return pow(x,y//2) * pow(x,y//2)
    else:
        return pow(x,y//2) * pow(x,y//2) * x


print(pow(2,9))