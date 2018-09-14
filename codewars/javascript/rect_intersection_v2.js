/**
 * 
 * @param {number[][]} recs
 * @returns {number}
 */
function sumIntervals(intervals, end) {
    function max(a, b) { 
      return a > b? a: b;
    }
    if (end == 0) return 0
    sarr = intervals.sort((a,b) => a[0] - b[0])
	  //console.log('start' + intervals)
    prev = sarr[0]
    res = []
    for (let i = 1; i < end; i++) {
        if (sarr[i][0] < prev[1]) {
          prev = [prev[0], max(sarr[i][1], prev[1])]
        }
        else {
          res.push(prev)
          prev = sarr[i]
        }
    } 
    res.push(prev)
    //console.log(res)
    return res.reduce((res, v)=> v[1] - v[0] + res, 0)
}

function delete_interval(intervals, rec, end)
{
/*
	for (let i = 0; i < end; i++) {
		if (intervals[i][0] == rec[1] && intervals[i][1] == rec[3]) {
			delete(intervals[i])
			return
		}
	}
	return
 */
 //  console.log('delete ', intervals, rec)
	let lo = -1
	let hi = end-1
	while ((hi-lo) > 1) {
		let mid = lo + ~~((hi-lo)/2)
		if (intervals[mid][0] >= rec[1]) 
			 hi = mid
		else 
			 lo = mid
   }
   for (let j = hi; ;j++) {
     if (intervals[j][0] == rec[1] && intervals[j][1] == rec[3]) {
       delete (intervals[hi])
       break
     }
    }
}

function calculate(recs){
  if (recs.length == 0) return 0
	let arr = []
	for (let i = 0; i < recs.length; i++) {
		arr.push([recs[i][0], recs[i]])
		arr.push([recs[i][2], recs[i]])
	}
	let intervals = []
	arr = arr.sort((a,b)=>a[0] - b[0])
	//console.log(arr)
	intervals.push([arr[0][1][1], arr[0][1][3]])
	let ic = 1
	let union = 0
	for (i = 1; i < arr.length; i++) {
		//console.log('arry ', arr[i])
		rec = arr[i][1]
		dy = sumIntervals(intervals, ic)
		dx = arr[i][0] - arr[i-1][0]
		union += dy * dx
		if (arr[i][0] == rec[0]) { // new event
			intervals.push([rec[1], rec[3]])
			ic++;
		}
		else {		//end of event
			//console.log('delete ', intervals, rec)
			delete_interval(intervals, rec, ic)
			//console.log('delete ', intervals)
			ic--
		}
	}
	return union
}
console.log(calculate([1,1,4,5]))
