
var SegmentTree = function (n) { //arr) {
	this.n = n
	this.tree = [] //new Array(n+1)
	for (let i = 0; i < n; i++) 
		this.tree[n+i] = 0 //arr[i]

	// segment tree construction
	for (i = n-1; i >= 0; i--) 
		this.tree[i] = this.tree[i<<1] + this.tree[(i<<1)|1]

	this.query = function(l, r) {
		let res = 0
		for (l += this.n, r += this.n+1; l < r; l >>= 1, r >>= 1) {
			if (l&1) res += this.tree[l++]
			if (r&1) res += this.tree[--r]
		}
		return res
	}
	
	this.update = function(l, r, value) {
		for (let i = l; i <= r; i++)
			this.updatepoint(i, value)
	}

	this.updatepoint = function(p, dvalue) {
		p += this.n
		this.tree[p] += dvalue  
		this.tree[p>>1] = (this.tree[p] ? 1: 0)  + (this.tree[p^1]? 1: 0)
		for (p >>= 1; p > 0; p >>= 1) 
			this.tree[p>>1] = this.tree[p] + this.tree[p^1]
	}
	this.totalsum = function() {
		return this.tree[1]
	}
}

//var st = new SegmentTree(20)//[1,2,3,4,5,6,7,8,9,10,11,12,13])
//console.log(st.query(2,3))
//st.update(3, 5-1, 1)
//st.update(3, 9-1, 1)
//console.log(st.tree[1])
//st.update(3, 5-1, -1)
//console.log(st.tree[1])

function calculate(recs) {
	if (recs.length == 0) return 0
	let X = []
	let rec = recs[0]
	let ymin = rec[1]
	let ymax = rec[3]
	X.push([rec[0], true, rec])
	X.push([rec[2], false, rec])
	for (let i = 1; i < recs.length; i++) {
		let x0 = recs[i][0]
		let y0 = recs[i][1]
		let x1 = recs[i][2]
		let y1 = recs[i][3]
		X.push([x0, true, recs[i]])
		X.push([x1, false, recs[i]])
		if (y0 < ymin) ymin = y0
		if (y1 > ymax) ymax = y1
	}
	console.log(ymax-ymin+1)
	let st = new SegmentTree(ymax-ymin+100)
	X = X.sort((a, b) => a[0] - b[0])
	let prevx = X[0][0]
	let area = 0
	console.log(X)
	for (i = 0; i < X.length; i++) {
		console.log(X[i])
		let rec = X[i][2]
		let first = X[i][1]
		let currx = X[i][0]
		y0 = rec[1]
		y1 = rec[3]
		dy = st.totalsum()			
		dx = currx - prevx
		area += dy * dx
//		console.log('area: ', area, 'dy: ', dy, 'dx: ', dx, 'y0 ', y0, 'y1: ', y1)
//		console.log(st.tree)
		if (first) { 
			st.update(y0, y1-1, 1)
			console.log('insertion')
		}
		else {
			st.update(y0, y1-1, -1)
			console.log(st.tree[1])
			console.log('removal')
		}
		prevx = currx

	}
	return area
}
//console.log(calculate([[1,1,4,5]]))
console.log(calculate([[3,3,8,5], [6,3,8,9],[11,6,14,12]]))
