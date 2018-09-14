def format_duration(seconds):
    y = seconds / (365 * 24 * 60 * 60) 
    seconds -= y * 365 * 24 * 60 * 60
    d = seconds / (24 * 60 * 60) 
    seconds -= d * (24 * 60 * 60)
    h = seconds / (60 * 60)
    seconds -= h * (60 * 60)
    m = seconds / 60
    seconds -= m * 60 
    
    arr = [(y, "year"), (d, "day"), (h, "hour"), (m, "minute"), (seconds, "second")]
    arr = [(a[0], a[1] + "s" if a[0] > 1 else a[1]) for a in arr]
    #print(arr)
    arr = filter(lambda x: x[0] != 0, arr)
    res = ", ".join([str(a[0]) + " " + a[1] for a in arr[:-1]])
    if len(arr) > 1:
        res += " and "
    res += str(arr[-1][0]) + " " + arr[-1][1]
    return res
    print(res)
        
print(format_duration(365*24*60*60+2))
