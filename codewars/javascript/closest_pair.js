
function closest(numbers, lo, hi) {
	if (hi <= lo) 
		return [Number.MAX_VALUE, [], []]

	let mid = lo + Math.floor((hi - lo)/2)
	let [d1, q, r] = closest(numbers, lo, mid)
	let [d2, s, t] = closest(numbers, mid+1, hi)

	let dmin = Math.min(d1, d2);
	let odmin = dmin
	xmid = numbers[mid][0]
	aux = []
	for (let k = lo; k <= hi; k++) {
		if (Math.abs(numbers[k][0] - xmid) < dmin)
			aux.push(numbers[k])
	}
	p = aux.sort(function (a, b) { return a[1] - b[1]; })
	let pl = p.length
	let u, v
	for (let i = 0; i < pl; i++) {
		for (let j = i+1; j < pl && ((p[j][1]-p[i][1]) < dmin); j++) {
			let d = dist(p[i], p[j]) 
			if (d < dmin) {
				dmin = d
				u = p[i]
				v = p[j]
			}
		}
	}
	if (dmin < odmin) 
		return [dmin, u, v]

	if (odmin == d1)
		return [d1, q, r]
	else
		return [d2, s, t]
}

pts =[]
for (let i = 0; i < 1000; i++)
	pts.push([i/1000, i])
var dist;
// Calculate a pair of closest points in linearithmic time
function closestPair(points, calculateDistance) {
  dist = calculateDistance
  return closest(points.sort(function (a, b) { return a[0] - b[0]; }), 0, points.length-1).slice(1)
}

var count = 0
function caldist(p, q) {
	count++
	return Math.sqrt(Math.pow(p[0]-q[0], 2) + Math.pow(p[1]-q[1], 2))
}

console.log(closestPair(pts, caldist))
console.log(count)


