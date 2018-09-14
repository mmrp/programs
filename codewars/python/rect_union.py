#!/usr/bin/python
import math
class SegmentTree(object):
    def __init__(self, intervals):
        n = len(intervals)
        self.points = [0] * 2 * n
        for p, interval in enumerate(intervals):
            self.points[2*p] =  interval[0]
            self.points[2*p+1] = interval[1]
        self.points = [0] + self.points

        self.points = sorted(self.points)

        # Trim duplicates 
        k = 0
        for p, v in enumerate(self.points):
            if v != self.points[k]:
                k += 1
                self.points[k] = v

        self.start = 1
        self.end   = k #2**int(math.ceil(math.log(k, 2)))
        np = len(self.points) + 1

        np  = 2**(int(math.ceil(math.log(k, 2)))+2)
        self.isum    = [0] * np
        self.counter = [0] * np

    def union(self):
        return self.isum[1]

    def insert_interval(self, v0, v1):
        self.insert_edge(1, self.start, self.end, v0, v1, 1)

    def remove_interval(self, v0, v1):
        return self.insert_edge(1, self.start, self.end, v0, v1, -1)

    def insert_edge(self, node, left, right, v0, v1, inc, msg = ""):
        # going beyond [left, right]
        if v1 < self.points[left] or self.points[right] < v0:
            return

        lchild = 2 * node
        rchild = 2 * node + 1
        # [v0 <= left <= right <= v1], update node at this position
        if v0 <= self.points[left] and self.points[right] <= v1:
            self.counter[node] += inc
            if self.counter[node]:
                self.isum[node] = self.points[right] - self.points[left]
            else:
                self.isum[node] = self.isum[lchild] + self.isum[rchild]
            return

        # reached the last non-leaf node
        if left + 1 == right: return

        mid = (left + right) // 2

        #traverse left subtree
        self.insert_edge(lchild, left, mid, v0, v1, inc, "left")

        #traverse right subtree
        self.insert_edge(rchild, mid, right, v0, v1, inc, "right")

        # --> a counter is valid, if it had encountered a full enclosing interval in the past
        # if as a parent, if an update is needed and counter is valid, that means 
        # 1. Overlapping occuring
        # 2. Current interval is part of the earlier full enclosing interval
        # so store only the full enclosing interval
        # if no earlier enclosing interval, use the sum of children values
        if self.counter[node]:
            self.isum[node] = self.points[right] - self.points[left]
        else:
            self.isum[node] = self.isum[lchild] + self.isum[rchild]
        return

def rectangle_union(rect):
    hpoints = []
    vpoints = []
    for r in rect:
        hpoints += [[r[0], r]]
        hpoints += [[r[2], r]]
        vpoints += [[r[1], r[3]]]
    hpoints = sorted(hpoints)
    tree = SegmentTree(vpoints)
    cx, r = hpoints[0]
    _, y0, _, y1 = r
    tree.insert_interval(y0, y1)
    area = 0
    px = cx
    for cx, r in hpoints[1:]:
        area += tree.union() * (cx - px)
        px = cx
        x0, y0, x1, y1 = r
        if cx == x0:   #left edge
            tree.insert_interval(y0, y1)
        else:           #right edge
            tree.remove_interval(y0, y1)
#        print(area)
    return area

from collections import namedtuple
def brute_rectangle_union(rect):
    r = namedtuple('rectangle', 'x0 y0 x1 y1')
    def common_area(r1, r2):
#        print(r1, r2)
        a = 0
        if r1.x0 <= r2.x0 and r2.x0 < r1.x1:
            dx = min(r2.x1, r1.x1) - r2.x0
            if r1.y0 <= r2.y0 and r2.y0 <= r1.y1:
                dy = min(r2.y1, r1.y1) - r2.y0
                a = dx * dy
            elif r1.y0 <= r2.y1 and r2.y1 <= r1.y1:
                dy = (r2.y1 - max(r2.y0, r1.y0))
                a = dx * dy
            else:
                a = common_area(r2, r1)
        elif r2.x0 <= r1.x0 and r1.x0 < r2.x1:
            a = common_area(r2, r1)
        else:
            a = 0   #no intersection

#        print(r1, r2, a)
        return a
    carea = 0
    n = len(rect)
    for i in range(n):
        for j in range(i+1, n):
            carea += common_area(r(*rect[i]), r(*rect[j]))
    return sum([common_area(r(*R), r(*R)) for R in rect]) - carea


#rect = [[3,3,4,4], [3,1,4,5]]
#rect = [[1,1,2,2], [3,3,4,4], [5,5,6,6], [2, 2, 4, 5], [3, 1, 5, 4], [3,1,4,5]]
print(rectangle_union(rect))
print(brute_rectangle_union(rect))
