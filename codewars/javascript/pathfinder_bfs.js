function pathFinder(maze)
{
    maze = maze.split("\n").join("")
    let N    = ~~(Math.sqrt(maze.length))
    let visited = {}
    let nbrs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    let queue = []
    queue.push([0, 0, 0])
    let x, y, path
    while (queue.length) {
        [x, y, path] = queue.shift()
        if (x == N-1 && y == N-1) {
            if (maze[x * N + y] == '.')
                    return path
            continue
        }
        for (let i = 0; i < 4; i++) {
            let d = nbrs[i]
            let nx = x + d[0]
            let ny = y + d[1]
            if (nx < 0  || nx >= N || ny < 0 || ny >= N
                        || maze[nx*N+ny] == 'W'
                        || visited[[nx, ny]])
              continue
            queue.push([nx, ny, path+1])
            visited[[nx,ny]] = true
        }
    }
    return false
}
