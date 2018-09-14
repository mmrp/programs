function pathFinder(maze)
{
	maze = maze.split("\n").join("")
	N = ~~(Math.sqrt(maze.length))
	visited = {}
	let nbrs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

	function dfs(x, y)
	{
		if (x == N-1 && y == N-1) {
			if (maze[x * N + y] == '.')
				return true
			return false
		}
		visited[[x,y]] = true
		for (let i = 0; i < 4; i++) {
			let d = nbrs[i]
			let nx = x + d[0]
			let ny = y + d[1]
			if (nx < 0  || nx >= N || ny < 0 || ny >= N 
					|| maze[nx*N + ny] == 'W'
					|| visited[[nx, ny]])
				continue
			if ((r = dfs(nx, ny)))
				return r
		}
		return false
	}
	return dfs(0, 0, maze)
}

