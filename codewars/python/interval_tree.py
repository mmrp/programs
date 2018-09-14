#!/usr/bin/python3

class Node(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.max = y
        self.left = None
        self.right = None

    def intersects(self, interval):
        lo, hi = interval
        if self.y <= lo or hi <= self.x:
            return False
        return True


class IntervalTree(object):
    def __init__(self):
        self.root = None


    def __insert(self, h, interval):
        if h is None: return  Node(*interval)

        x, y = interval
        if    x <  h.x: h.left  = self.__insert(h.left, interval)
        else:           h.right = self.__insert(h.right, interval)

        if y > h.max: h.max = y
        return h

    def insert(self, interval):
        self.root = self.__insert(self.root, interval)


    def inorder(self, h, res=''):
        if h is None: return res

        res = res + "[" + str(h.x) + ':' + str(h.y) + ":" + str(h.max) + "]" + " "
        res = self.inorder(h.left, res)
        res = self.inorder(h.right, res)
        return res

    def __repr__(self):
        return self.inorder(self.root)

    def search(self, h, interval, res=[]):
        if h is None:
            return []
        if h.intersects(interval):
            res += [[h.x, h.y]]

        lo, hi = interval
        if h.right and h.right.max > lo:
            self.search(h.right, interval, res)

        if h.left and h.left.max > lo:
            self.search(h.left, interval, res)

        return res

    def delete(self, h, interval):
        pass

    def searchall(self, interval):
        return self.search(self.root, interval)

if __name__ == '__main__':
    it = IntervalTree()
    for e in [[17, 19], [1, 25], [5,8], [4, 8], [15, 18],[7, 10], [16, 22], [21, 24]]:
        it.insert(e)
    print(it)
    print(it.searchall([4, 10]))
    pass
