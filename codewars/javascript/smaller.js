function merge(A, B, C) {
    var p = A.length
    var q = B.length
    var i = 0
	var j = 0
    var res = []
    while ( i < p && j < q) { 
        if (B[j][0] >= A[i][0]) {
            res.push(B[j])
            j++
        }
        else {
            k = A[i][1]
            C[k] += q - j
            res.push(A[i])
            i++
        }   
    }
    while (i < p) {
      res.push(A[i])
      i++
    }
    
    while (j < q) {
      res.push(B[j])
      j++
    }
    return res
}

function mergesort(A, C) {
    if (A.length == 1) 
      return A
    m = A.length/2
	var a1 = A.slice(0, m)
	var a2 = A.slice(m, A.length)
    var A1 = mergesort(a1, C)
    var B1 = mergesort(a2, C)
    A = merge(A1, B1, C)
    return A
}

function smaller(arr) {
  var narr = []
  for (var i = 0; i < arr.length; i++) {
      narr.push([arr[i], i])
  }
  var carr = new Array(arr.length).fill(0)
  var res = mergesort(narr, carr)
  return carr
}

var testarr = new Array(100000);

var T0 = performance.now();
for (var count = 0; count < 100; count++) {
	maximum = 100000
	minimum = 0
	for(var i = 0; i < 100000; i++) {
		testarr[i] = Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;
	var t0 = performance.now();
	smaller(testarr) //[10,6,3,7,6,1,3,10,10,7]))
	var t1 = performance.now();
	console.log("Call to doSomething took " + (t1 - t0) + " milliseconds.")
}
var T1 = performance.now();
console.log("Call to doSomething took " + (T1 - T0) + " milliseconds.")
