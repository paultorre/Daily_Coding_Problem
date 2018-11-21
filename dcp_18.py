inp = [10, 5, 2, 7, 8, 7]
ans = []

m = max(inp[0],inp[1],inp[2])

ans.append(m)

i = 3
while i < len(inp):
  m = max(inp[i],inp[i-1],inp[i-2])
  ans.append(m)
  i += 1
print(ans)
