import re
m = r'^(0|101|11(01)*(1|00)1|(100|11(01)*(1|00)0)(1|0(01)*(1|00)0)*0(01)*(1|00)1)+$'

for i in range(10000):
    if re.match(m, bin(i)[2:]) and i % 5 != 0:
        print('screwed', i, bin(i)[2:])



