def same_structure_as(original,other):
    def get(o):
        s = ""
        for e in o:
            #print(type(e))
            if isinstance(e, list):
                #print('am here')
                s += "(" + get(e) + ")"
            else:
                s += "1"
        return(s)
    print(original, get(original), other, get(other))
