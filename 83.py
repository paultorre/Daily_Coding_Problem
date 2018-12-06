#   Recursively swaps the two children of a root from the bootom up using a postorder traversal
#   Checked by doing an inorder traversal before and after swapping, verifying that post swapping order was backwards from original
#   
#   Time - O(V+E)
#   Space - O(log V)   (implicit call stack memory)


class Node:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def swap(root):
    if not root:
        return
    if root.left is None and root.right is None:
        return
    swap(root.left)
    swap(root.right)
    t = root.left
    root.left = root.right
    root.right = t

def inorder(arr,root):
    if not root:
        return
    inorder(arr,root.left)
    arr.append(root.val)
    inorder(arr,root.right)

r = Node('a')
r.left = Node('c')
r.left.right = Node('f')
r.right = Node('b')
r.right.left = Node('e')
r.right.right = Node('d')

a = []
inorder(a,r)

swap(r)

a2 = []
inorder(a2,r)

print(a)
print(a2)