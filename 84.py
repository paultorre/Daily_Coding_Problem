# Boils down to how many connected components there are.
# For each spot in the grid, look if there is land.  if there is, run a DFS starting from that piece of land and manipulate the grid to reflect that
# that piece of land has been visited.  The number of islands will be equal to the number of connected components
#  in the grid.  NOTE: This algorithm counts diagonal land masses as being connected.
#
#  Time: O(n^2)
#  Space: O(1)

def dfs(arr,i,j):
    stack = [(i,j)]
    while stack:
        #print(stack)
        t = stack.pop()
        row = t[0]
        col = t[1]
        arr[row][col] = 0
        stack.append((row-1,col-1)) if row > 0 and col > 0 and arr[row-1][col-1] == 1 else None
        stack.append((row-1,col)) if row > 0 and arr[row-1][col] == 1 else None
        stack.append((row-1,col+1)) if row > 0 and col < len(arr[0])-1 and arr[row-1][col+1] == 1 else None
        stack.append((row,col-1)) if col > 0 and arr[row][col-1] == 1 else None
        stack.append((row,col+1)) if col < len(arr[0])-1 and arr[row][col+1] == 1 else None
        stack.append((row+1,col-1)) if row < len(arr)-1 and col > 0 and arr[row+1][col-1] == 1 else None
        stack.append((row+1,col)) if row < len(arr)-1 and arr[row+1][col] == 1 else None
        stack.append((row+1,col+1)) if row < len(arr)-1 and col < len(arr[0])-1 and arr[row+1][col+1] == 1 else None


def islands(arr):
    ans = i = 0
    while i < len(arr):
        j = 0
        while j < len(arr[0]):
            if arr[i][j] == 1:
                dfs(arr,i,j)
                ans += 1
            j += 1
        i += 1
    return ans


a = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
i = 0
while i < len(a):
    j = 0
    while j < len(a[0]):
        a[i][j] = int(a[i][j])
        j += 1
    i += 1

for row in a:
    print(row)
print(islands(a))