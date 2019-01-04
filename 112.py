class Node(object):
    def __init__(self,x):
        self.data = x
        self.p = None
        self.left = None
        self.right = None

def find_lca(a,b):
    """ Finds LCA of 2 given nodes, assuming they hold pointers to their parents.

        Args:
            a: node
            b: node
        
        Returns:
            Pointer to LCA

    """
    a_path = set()
    while a is not None:
        a_path.add(a)
        a = a.p

    while b is not None:
        if b in a_path:
            return b
        b = b.p

root = Node('a')
root.left = Node('b')
root.left.p = root
root.right = Node('c')
root.right.p = root

root.right.right = Node('d')
root.right.right.p = root.right

print(find_lca(root.left,root.right.right).data)