var res = new Array(100000)
function merge(A, l, h, C) {
	var m = ~~((l+h)/2)
    var p = m 
    var q = h

    var i = l
	var j = m+1
	var k = 0
	var s
    while (i <= p && j <= q) { 
        if (A[j][0] >= A[i][0]) {
            res[k] = A[j]
            j++
        }
        else {
            s = A[i][1]
            C[s] += q - j + 1
            res[k] = A[i]
            i++
        }   
		k++
    }
    while (i <= p) res[k++] = A[i++]
    while (j <= q) res[k++] = A[j++]
	for (var i = 0; i < k; i++) 
		A[l+i] = res[i]
    
}

function mergesort(A, l, h, C) {
	if (l < h) {
		var m = ~~((l+h)/2)
		mergesort(A, l, m, C)
	    mergesort(A, m+1, h, C)
		merge(A, l, h, C)
	}
}

function smaller(arr) {
  var narr = new Array(arr.length)
  for (var i = 0; i < arr.length; i++) 
      narr[i] = [arr[i], i]
  
  var carr = new Array(arr.length).fill(0)
  var res = mergesort(narr, 0, arr.length-1, carr)
  console.log(arr, narr)
  return carr
}

var testarr = new Array(100000);

var T0 = performance.now();
for (var count = 0; count < 100; count++) {
	maximum = 100000
	minimum = 0
	for(var i = 0; i < 100000; i++) 
		testarr[i] = Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;
	var t0 = performance.now();
	console.log(smaller(testarr)) //[10,6,3,7,6,1,3,10,10,7]))
	var t1 = performance.now();
	console.log("Call to doSomething took " + (t1 - t0) + " milliseconds.")
}
var T1 = performance.now();
console.log("Call to doSomething took " + (T1 - T0) + " milliseconds.")
