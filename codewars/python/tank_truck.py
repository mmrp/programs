#!/usr/bin/python

"""
volume   of cylinder = vt
diameter of cylinder = d => r = d/2

depth/height of cylinder => pi * r * r * depth = vt
=> depth = vt /(pi * r * r)


height of liquid = h


volume of liquid = area of liquid * depth

|\ <- angle
| \
|  \
|___\


area of liquid = (area_of_arc - area of triangle)

area_of_arc = pi * r * r * (angle_deg)/360

angle_deg = cos_inv(r/(r-h))

area of triangle = 1/2 * sqrt(r*r - (r-h)**2)* (r-h)  
                 = 1/2 * sqrt(2*r*h - h*h)* (r-h)


volume of liquid = ((pi * r * r * cos_inv(r/r-h)/360) - (1/2 * sqrt(2*r*h - h*h) * (r-h))) * vt/(pi * r * r)
                 = (cos_inv(r/r-h)/360 * vt) - (1/2 * sqrt (2*r*h - h * h) * (r-h) * vt /(pi * r * r))
"""

import math
def tankvol(h, d, vt):

    r = d/2
    angle = math.acos((r-h)/r * 1.0)    # radians
    
    tri_area = 1/2 * math.sqrt(2 * r * h - h * h) * (r-h)
    arc_area = math.pi * r * r * math.degrees(angle)/360
    
    liquid_area = 2 * (arc_area - tri_area)

    depth = (vt)/(math.pi * r * r)
    liquid_volume = liquid_area * depth

    return liquid_volume


print(tankvol(5, 7, 3848))
