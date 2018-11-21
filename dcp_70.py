ans = 0
n = 0
t = 0
while ans < n:
    if sum([int(c) for c in str(t)]) == 10:
        ans += 1
    t += 1
print(t-1)
