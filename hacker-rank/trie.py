_last = '_last'
root = dict()
def add_name(word):
    current = root
    for w in word:
        current = current.setdefault(w, {})
    current[_last] = _last

    
def count_last(d):
    c = 0
    for e in d:
        if '_last' == e:
            c += 1
        else:
            c += count_last(d[e])
    return c

def find_name(word):
    current = root
    for w in word:
        if w not in current:
            print(0)
        else:
            current = current[w]
    else:
        #print(current)
        print(count_last(current))
    
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        add_name(contact)
    elif op == 'find':
        print('fid')
        find_name(contact)
