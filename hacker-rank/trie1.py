_last = '_last'
class Node:
    def __init__(self):
        self.d = {}
        self.count = 0

root = Node()
def add_name(word):
    current = root
    for w in word:
        if w not in current.d:
            current.d[w] = Node()
        current.d[w].count += 1
        current = current.d[w]
    else:
        current.d[_last] = _last

def find_name(word):
    current = root
    for w in word:
        if w not in current.d:
            print(0)
            return
        else:
            current = current.d[w]
    else:
        print(current.count)
    
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        add_name(contact)
    elif op == 'find':
        print('fadding name')
        find_name(contact)
