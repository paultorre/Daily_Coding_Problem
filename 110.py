class Node(object):
    """ Simple Binary Tree Node object class"""
    def __init__(self,x):
        self.data = x
        self.left = None
        self.right = None



def enum_paths(root):
    """ Returns all paths from root to leaves in a binary tree.
    
        Leverages a Depth First Search to traverse and record all paths.

        Args:
            root: Node object representing the root of the binary tree.

        Returns:
            A list containing the paths (lists) from root to leaf.
    """
    stack = [root]
    paths,p = [], []
    while stack:
        t = stack.pop()
        p.append(t.data)
        if t.left is None and t.right is None:
            paths.append([x for x in p])
            p.pop()
        else:
            stack.append(t.right) if t.right else None
            stack.append(t.left) if t.left else None
    return paths
    

#   Test the code.
#
#    1
#   / \
#  2   3
#     / \
#    4   5
#
# Returns: [[1, 2], [1, 3, 4], [1, 3, 5]]

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

print(enum_paths(root))