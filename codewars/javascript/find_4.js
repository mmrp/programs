
function get_2sum(arr) {
	sum2 = new Array(arr.length)
	k = 0
	for (let i = 0; i < arr.length; i++) 
		for (let j = i+1; j < arr.length; j++) 
			sum2[k++] = [i, j, arr[i]+arr[j]]	
	return sum2
}

function commonindex(arr, i, j) {
	console.log('index', arr[i], arr[j])
	if (arr[i][0] == arr[j][0] || arr[i][1] == arr[j][1] ||
		arr[i][0] == arr[j][1] || arr[i][1] == arr[j][0])
		return true
	return false
}

function any(a, arr, l, h, val) {
	res =  [arr[l][0], arr[l][1],arr[h][0], arr[h][1]].map((v,i,a1) => a[v]).some((v,i,a) => v == val)
	console.log(res)
	return res
}
function find4sum(a, arr, v) {
	let l = 0
	let h = arr.length-1
	sum = 2 * v
	while (l < arr.length && h >= 0) {
		csum = arr[l][2] + arr[h][2]
		console.log(csum, sum)
		console.log([arr[l][0], arr[l][1],arr[h][0], arr[h][1]].map((v,i,a1) => a[v]))
		if (csum == sum && !commonindex(arr, l, h) && any(a, arr,l,h,v)) {
			return v
		}
		else 
		if (csum < sum) 
			l++
		else
			h--
	}
	return null
}


//arr = [1,2,3,4,5,6, 12, 17]
//arr = [ -10, -5, -3, -2, 0 ]
arr = [ -100,-1,0,7,101]
sum2 = get_2sum(arr)
console.log(sum2)
for (let i = arr.length-1; i >= 0; i--) {
	res = find4sum(arr, sum2, arr[i])
	if (res != null)
		console.log('output', res)
//	if (res)
//		console.log(res.map((v,i,a) => arr[v]), arr[i])
}
