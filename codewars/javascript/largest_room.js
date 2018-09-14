function largestRoomArea1(rooms) {

  function bfs(rooms, i, j, k) {
    let rmax = rooms.length
    let cmax = rooms[0].length
    let q = [[i,j]]
    let count = 0
    let dirs = [[1,0],[-1,0], [0,1],[0,-1]]
    rooms[i][j] = k
    while (q.length > 0) {
      let p = q.pop(0)
      count++
      for (let d = 0; d < 4; d++) {
        let dr = p[0] + dirs[d][0]
        let dc = p[1] + dirs[d][1]
		console.log(dr, dc)
        if (dr >= rmax || dr < 0 || dc >= cmax || dc < 0 || rooms[dr][dc] != 0)
            continue
		rooms[dr][dc] = k
		q.push([dr, dc])
      }
    }
    return count;
  
  }
  let m = 0;
  let k = 2
  function max(a, b) { return a > b ? a: b; }
  for (let i = 0; i < rooms.length; i++) {
    for (let j = 0; j < rooms[0].length; j++) {
      if (rooms[i][j] == 0) {
        m = max(m, bfs(rooms, i, j, k++))
	  }
    }
  }
  console.log(rooms)
  return m;  
}

function largestRoomArea(rooms) {
	function fill(i, j) { 
		return (rooms[i]|[])[j] == '0'?  (rooms[i][i] = 1) + fill(i+1, j) + fill(i-1, j) + fill(i, j+1) + fill(i, j-1): 0;		  }
	return rooms.reduce((l, x, i) => x.reduce((l, x, j) => Math.max(l, fill(i, j), l), 0))
}

console.log(largestRoomArea(
[[1,1,1,1,1,1], 
 [1,0,1,0,0,1], 
 [1,0,1,0,0,1], 
 [1,1,1,1,1,1]]))
console.log(largestRoomArea([[1,0], [0, 1]])) //,1,1,1,1], [1,0,1,0,0,1], [1,0,1,0,0,1], [1,1,1,1,1,1]]))
