ans = 0
n = 0
t = 0
while ans < n:
    if sum([int(c) for c in str(t)]) == 10:
        ans += 1
    t += 1


'''efficient version'''
ans = 0
n = 2
t = 19
while ans < n:
    if sum([int(c) for c in str(t)]) == 10:
        ans += 1
    t += 9
    
print(t-9) if n > 0 else print(0)
