i = 0
j = 1
words = ['quick', 'brown', 'the', 'fox']
s = 'thequickbrownfox'
ans = []
while i < len(s):
	if s[i:j] in words:
		ans.append(s[i:j])
		i = j
		j += 1
	else:
		j += 1

print(ans)
