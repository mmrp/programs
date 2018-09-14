var res = new Array(100000)
function merge(A, l, h, C) {
	var m = ~~((l+h)/2)
  var p = m 
  var q = h
  var i = l
	var j = m+1
	var k = 0
  while (i <= p && j <= q) { 
      if (A[j][0] >= A[i][0]) {
          res[k] = A[j]
          j++
      }
      else {
          var s = A[i][1]
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
  if (h-l < 0) {
    if (A[h][0] < A[l][0]) {
      C[A[l][1]]++
    }
    else {
      c = A[l]
      A[l] = A[h]
      A[h] = c
    }
    return
  }
  
	if (l < h) {
		var m = ~~((l+h)/2)
		mergesort(A, l, m, C)
	  mergesort(A, m+1, h, C)
		merge(A, l, h, C)
	}
}
var carr = new Array(100000)
var narr = new Array(100000)
//for (var i = 0; i < narr.length; i++)
//    narr[i] = [0, i]
function smaller(arr) {
  //var narr = new Array(arr.length)
  for (var i = 0; i < arr.length; i++) {
      narr[i] = [arr[i], i]
      carr[i] = 0
  }
  //var carr = new Array(arr.length).fill(0)
  var res = mergesort(narr, 0, arr.length-1, carr)
  //console.log(arr, narr)
  return carr.slice(0, arr.length)
}

