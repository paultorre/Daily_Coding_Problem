#   Check every row and every column
#   Time - O(N^2) 
#   Space - O(1)

def is_in_mat(query,mat):
    for row in mat:
        if ''.join(row) == query:
            return True
    j = 0
    while j < len(mat[0]):
        i = 0
        s = ''.join([mat[i][j] for i in range(len(mat))])
        if s == query:
            return True
        j += 1
    return False

def is_in_mat_with_hash(query,mat):
    memo = set()
    for row in mat:
        memo.add(''.join(row))
    
    j = 0
    while j < len(mat[0]):
        i = 0
        memo.add(''.join([mat[i][j] for i in range(len(mat))]))
        j += 1

    return query in memo

a = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

print(is_in_mat('MASS', a))
print(is_in_mat_with_hash('MASS', a))