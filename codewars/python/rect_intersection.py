#!/usr/bin/python

from collections import namedtuple
Point = namedtuple('point', 'x1 x2')

def get_common_length(l, m):
    if m.x2 < l.x2:
        return m.x2 - m.x1
    else:
        return l.x2 - m.x1

def find_intersection_length(points):
    npoints = []
    for p in points:
        npoints.append((p.x1, p))
        npoints.append((p.x2, p))

    spoints = sorted(npoints)
    bag = set([])
    bag.add(spoints[0][1])
    tlen = 0
    for _, p in spoints[1:]:
        if p in bag:
            bag.remove(p)
            continue
        #found an intersection
        for bp in bag:
            tlen += get_common_length(bp, p)
        bag.add(p)
    print(tlen, len(bag))
    return tlen


find_intersection_length((Point(2, 8), Point(1,4), Point(2, 10), Point(3, 5)))
