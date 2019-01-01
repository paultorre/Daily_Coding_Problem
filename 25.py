s = 'chats'
re = '.*at'

for i,c in enumerate(re):
    if c == '.':
        continue
    if c == '*':
        continue
    if c != s[i]:
        print('False')
print('True')
