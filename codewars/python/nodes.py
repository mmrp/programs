class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

def tree_to_list(tree_root):
    l = []
    nodes = [tree_root]
    while nodes:
        head = nodes.pop(0)
        l.append(head.data)
        if head:
            for n in head.child_nodes:
                nodes.append(n)
    return l

tree_to_list(Node(1, [Node(2, [Node(3), Node(4), Node(5)]), Node(3, [Node(7)])])) 
#[1, 2, 3, 3, 4, 5, 7])
