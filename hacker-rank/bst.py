class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def traverse(root, minv, maxv):
    if not root:
        return True

    return minv < root.data and root.data < maxv and \
    checkBST(root.left, minv, min(maxv, root.data)) and \
    checkBST(root.right, max(minv, root.data), maxv)



def checkBST(root):        
     return traverse(root, -1, 10001)

def print_tree(root):
    if root:
        print_tree(root.left)
        print_tree(root.right)
        print(root.data)

if __name__ == '__main__':
    a = [node(d) for d in range(7)]
#a[2].data = a[1].data = 2
    a[5].left = a[4]
    a[4].left = a[3]
    a[4].left = a[1]
    a[1].left = a[0]
    a[3].left = a[2]
    a[5].right = a[6]
    print(checkBST(a[5]))
    print_tree(a[5])
