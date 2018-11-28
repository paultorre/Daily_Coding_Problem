def min_deletions(matrix):
    ans = 0

    # If there's only one row, then you do not need to delete anything.
    if len(matrix[0]) == 1:
        return ans

    # Construct each column. Sort it, then compare with the original column.  If they are different, then you must delete this row.
    # Time - O(MN) because of nested for loops.  Space - O(N)
    for col in range(len(matrix[0])):
        c = []
        for row in range(len(matrix)):
            c.append(matrix[row][col])

        temp = sorted(c)
        if c != temp:
            ans += 1
    return ans

matrix = [
    ['z','y','x'],
    ['w','v','u'],
    ['t','s','r'],
]

print(min_deletions(matrix))