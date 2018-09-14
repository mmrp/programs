import math
from collections import namedtuple

Point = namedtuple("Point", "x y")
class ConvexHull():
    def polar_angle(self, q):
        p = self.base
        if p.x == q.x:
            d = 90
        else:
            d = math.degrees(math.atan((p.y-q.y)*1.0/(p.x-q.x)))

        if d < 0:
            d += 180
        elif d == 0 and p.x > q.x:
            d = 180
        return (d, math.sqrt((p.x-q.x)**2+(p.y-q.y)**2))

    def __init__(self, points):
        self.points = [Point(p[0], p[1]) for p in sorted(points, key = lambda p: (p[1], -p[0]))]
        self.base   = self.points[0]
        k = 0
        while self.base == self.points[k]:
            k += 1
        self.polar = sorted(self.points[k:], key = self.polar_angle)

    def scan(self):
        hull = [self.base, self.polar[0]]
        for p in self.polar[1:]:
            while len(hull) > 1 and self.ccw(hull[-2], hull[-1], p) <= 0:
                hull.pop()
            hull.append(p)
        return hull


    def ccw(self, a, b, c):
        """
        +1 -> counter clockwise
        -1 -> clockwise
         0 -> collinear
        """
        area = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
        if area > 0: return 1
        if area < 0: return -1
        return 0

def hull_method(pointlist):
    ch = ConvexHull(pointlist)
    return [[p.x, p.y] for p in ch.scan()]
