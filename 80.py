import collections

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


d = collections.defaultdict(list)

# Use a BFS
# This iterative BFS will keep exectuing until there are no more nodes left to traverse.
# In this way, the LAST node it traverses must be the node with greatest depth.
# Time - O(V+E)
# Space - O(1)
def bfs(root):
    ans = 0
    q = [root]
    while q:
        t = q.pop(0)
        q.append(t.left) if t.left else None
        q.append(t.right) if t.right else None
        ans = t
    return ans

# Recursive Inorder solution.  
# Keep track of all levels and all nodes at each level in a dictionary.
# Finally, return the node at the max key (max depth)
# Time - O(V+E)
# Space - O(V)
def inorder(root,lvl):
    if not root:
        return
    inorder(root.left,lvl+1)
    d[lvl].append(root.val)
    inorder(root.right,lvl+1)

root = TreeNode('a')
root.left = TreeNode('b')
root.right = TreeNode('c')
root.left.left = TreeNode('d')

print('------- Inorder Recursive SOLUTION --------')
inorder(root,0)
m = max(d.keys())
print(d[m])

print('------- BFS SOLUTION --------')
print(bfs(root).val)


a = b = TreeNode('s')


print(a==b)