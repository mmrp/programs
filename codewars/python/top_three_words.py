#!/usr/bin/python

def top_3_words(str):
    lst = dict()
    for s in str.split():
        sl = s.lower()
        if sl not in lst:
            lst[sl] = 0
        lst[sl] += 1

    res = []
    for p, k in enumerate(sorted(lst, key = lst.get, reverse = True)):
        if p == 3:
            break;
        res.append(k)

    return res
    

print top_3_words("In a village of La Mancha, the name of which I have no desire to call to \
        mind, there lived not long since one of those gentlemen that keep a lance \
        in the lance-rack, an old buckler, a lean hack, and a greyhound for \
        coursing. An olla of rather more beef than mutton, a salad on most \
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra \
        on Sundays, made away with three-quarters of his income.")

