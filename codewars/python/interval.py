#!/usr/bin/env python3


class Node(object):
    def __init__(self, key, value, color, size):
        self.key   = key
        self.value = value
        self.left  = None
        self.right = None
        self.color = color
        self.size  = size
        self.mvalue = value

class RBTree(object):
    RED_COLOR = 1
    BLACK_COLOR = 2

    def __init__(self):
        self.root = None

    def size(self, h):
        if h is None:
            return 0
        return h.size

    def __isred(self, h):
        if h is None:
            return None
        return h.color == RBTree.RED_COLOR

    def __rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left  = h
        x.color = x.left.color
        x.left.color = RBTree.RED_COLOR
        x.size = h.size
        h.size = self.size(h.left) + self.size(h.right) + 1
        return x

    def __rotate_right(self, h):
        x = h.left
        h.left  = x.right
        x.right = h
        x.color = x.right.color
        x.right.color = RBTree.RED_COLOR
        x.size = h.size
        h.size = self.size(h.left) + self.size(h.right) + 1
        return x

    def __flip_color(self, color):
        if color == RBTree.RED_COLOR:
            return RBTree.BLACK_COLOR
        return RBTree.RED_COLOR

    def __flip_colors(self, h):
        h.left.color = self.__flip_color(h.left.color)
        h.right.color = self.__flip_color(h.right.color)
        h.color = self.__flip_color(h.color)

    def __insert(self, h, key, value):
        if h is None: return Node(key, value, RBTree.RED_COLOR, 1)

        if   key < h.key:
            h.left = self.__insert(h.left, key, value)
        elif key > h.key:
            h.right = self.__insert(h.right, key, value)
        else:
            h.value = value

        if self.__isred(h.right) and not self.__isred(h.left):
            h = self.__rotate_left(h)

        if self.__isred(h.left) and self.__isred(h.left.left):
            h = self.__rotate_right(h)

        if self.__isred(h.left) and self.__isred(h.right):
            self.__flip_colors(h)

        h.size = self.size(h.left) + self.size(h.right) + 1
        return h

    def put(self, key, value):
        self.root = self.__insert(self.root, key, value)


    def inorder(self, h, res = '', d = 0):
        if h is None:
            return res
        res = self.inorder(h.left, res, d+1)
        res = res + str(h.key) + ':' + str(d) + ':' + str(h.size) + ' '
        res = self.inorder(h.right, res, d+1)
        return res

    def __repr__(self):
        return 'rbtree ' + self.inorder(self.root)


if __name__ == '__main__':
    rb = RBTree()
    for e in [1,5,2,8,9,10,4,6]:
        rb.put(e, None)
    print(rb)
    pass
