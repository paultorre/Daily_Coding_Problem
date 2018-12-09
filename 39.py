import copy


#   Hard to check if this is correct.
#   Helper function to calculate the number of neighboring living cells according to rules,
#   careful to not go out of bounds.
#
#   Time - O(steps * )
#
#




def num_liv_neigh(i,j,b):
    ans = 0
    ans += 1 if i > 0 and j > 0 and b[i-1][j-1] == '*' else 0
    ans += 1 if i > 0 and b[i-1][j] == '*' else 0
    ans += 1 if i > 0 and j < len(b[0]) - 1 and b[i-1][j+1] == '*' else 0
    ans += 1 if j > 0 and b[i][j-1] == '*' else 0
    ans += 1 if j < len(b[0]) - 1 and b[i][j+1] == '*' else 0
    ans += 1 if i < len(b) - 1 and j > 0 and b[i+1][j-1] == '*' else 0
    ans += 1 if i < len(b) - 1 and b[i+1][j] == '*' else 0
    ans += 1 if i < len(b) - 1 and j < len(b[0]) - 1 and b[i+1][j+1] == '*' else 0
    return ans

def life(init, steps):
    mx = 0
    my = 0
    for c in init:
        mx = max(mx,c[0])
        my = max(my, c[1])
    
    #init board
    board = [ ['.'] * (my+1) for _ in range(mx+1)]
    for c in init:
        x,y = c[0],c[1]
        board[x][y] = '*'

    for day in range(steps):
        print('--------------- DAY: ', day, ' ---------------')
        for row in board:
            print(row)
        
        t = copy.deepcopy(board)
        i = 0
        while i < len(board):
            j = 0
            while j < len(board[0]):
                l_n = num_liv_neigh(i,j,board)
                if t[i][j] == '*':
                    if l_n < 2:
                        t[i][j] = '.'
                    elif l_n > 3:
                        t[i][j] = '.'
                elif l_n == 3:
                    t[i][j] = '*'
                j += 1
            i += 1
        board = t
        


init = [(1,1),(3,1),(3,0),(5,7),(2,2)]
life(init,9)
