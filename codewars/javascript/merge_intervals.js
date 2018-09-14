function sumIntervals(intervals){
    function max(a, b) { 
      return a > b? a: b;
    }
    sarr = intervals.sort((a,b) => a[0] - b[0])
    prev = sarr[0]
    res = []
    for (let i = 1; i < sarr.length; i++) {
        if (sarr[i][0] < prev[1]) {
          prev = [prev[0], max(sarr[i][1], prev[1])]
        }
        else {
          res.push(prev)
          prev = sarr[i]
        }
    } 
    res.push(prev)
    return res.reduce((res, v)=> v[1] - v[0] + res, 0)
}
