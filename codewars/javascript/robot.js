function getCommands(field, power) 
{
	var grid = []
	var w = ~~Math.sqrt(field.length)
	
	var start = field.indexOf('S')
	var end = field.indexOf('T')
	
	console.log('Start: ', start)
	
	var dir = [[-1, 0, 0], [1, 0, 2], [0, -1, 1], [0, 1, 3]]
	var dist = {}
	var visited = []
	var done = false

	dist[start] = [0, start, '']
	visited.push(start)

	while (!done && visited.length) {
		n = visited.shift()
		console.log('popped: ', n)
		var x, y;
		x = ~~(n/w)
		y = n % w;
		d = dist[n][0]
		for (var j = 0; j < dir.length; j++) {
			dx = x + dir[j][0]
			dy = y + dir[j][1]
			direction = dir[j][2]
			p = dx * w + dy
			if (dx >= 0 && dx < w && dy >= 0 & dy < w && field[p] != "#" && !dist[p]) {
				dist[p] = [d+1, n, direction];
				visited.push(p);
				if (p == end) {
					done = true
					break
				}
			}
		}
	}
	path = '' 
	if (done) {
		p = end
		console.log ("--path--")
		while (p != start) {
			console.log(p, dist[p][2])
			path += dist[p][2]
			p = dist[p][1]
		}
		var finalpath = ''
		path = path.split("").reverse()
		var cur = 0
		for (var i = 0; i < path.length; i++) {
			off = cur - path[i] 
			if (off == 3) 
				off = -1

			if (off == -3) 
				off = 1

			if (off > 0) {
				finalpath += 'r'.repeat(off)
			}
			else if (off < 0) {
				finalpath += 'l'.repeat(-off)
			}
			cur = path[i]
			finalpath += 'f'
		}
		console.log(p, dist[p][2])
		console.log ("--path--", path, finalpath)
		if (finalpath.length > power)
			return []

		return finalpath.split('')
	}
	return []
}

//console.log(getCommands('T.S.', 10))//.join('') //== 'f'
console.log(getCommands('T..#.#..S', 10))//.join('')// == 'rffrff'
console.log(getCommands('....S#.##....T#.')) //T..#.#..S', 10))//.join('')// == 'rffrff'
//getCommands('S.......T', 5).join('') //== ''
console.log(getCommands('S#.##...T', 20))//.join('') //== ''
