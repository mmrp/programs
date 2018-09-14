function intersection(m, p) {
	function min(a, b) {
		return a < b? a: b
	}
	console.log('am here', p, m)
	let len = 0
	for (let q in m) {
		q = q.split(",").map(w => parseInt(w))
		len += min(q[1], p[1]) - p[0]
		console.log('inhere', p, q, len)
	} 
	return len
}

function sumIntervals(intervals){
	let sarr = []
	let totallen = 0
	for(let i = 0; i < intervals.length; i++) {
		sarr.push([intervals[i][0], intervals[i]])	
		sarr.push([intervals[i][1], intervals[i]])	
		totallen += intervals[i][1] - intervals[i][0]
	}
	sarr = sarr.sort((a,b) => a[0] - b[0])
	console.log(intervals)
	let commonlen = 0	
	let m = {}
	for (let i = 0; i < sarr.length; i++) {
		let p = sarr[i][1]
		if (p in m && sarr[i][0] == p[1]) { 
			console.log('deleting ', p)
			delete m[p]
		}
		else {
			commonlen += intersection(m, p)
			m[p] = true
		}
	}	
	console.log(commonlen)
	console.log(totallen - commonlen)
	return totallen - commonlen
}
//sumIntervals([[1,2], [5, 10], [4, 6]])
//sumIntervals([[1,4],[7, 10],[3, 5]])
//sumIntervals([[1,5],[1,5]])
sumIntervals([ [ 2, 9 ], [ 2, 6 ], [ 2, 4 ]]) //, [ 2, 9 ], [ 2, 5 ] ])
