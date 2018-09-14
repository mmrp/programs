function findE(arr, l, h, v) {
	if (v < arr[l] || v > arr[h])
		return [false, l-1]
	//console.log('entry', l, h, v)
	while (l <= h) {
		let m = ~~((l+h)/2)
		//console.log('E', l, h, m)
		if (arr[m] < v) 
			l = m+1
		else
		if (arr[m] > v)
			h = m - 1
		else
			return [true, m];
	}
	return [false, (arr[h] < v)? h : h-1]
}

function findD(arr, k, length) {
//	console.log('k length', k, length)
	let rem1, rem2
	for (var i = 0; i < length; i++) {
		rem1 = k - arr[i]
		let e = arr.length-1
		for (var j = i+1; j <= e; j++) {
			rem2 = rem1 - arr[j]
			console.log(arr[i], arr[j], rem2);
			[r, e] = findE(arr, j+1, e, rem2)
			if (r) {
//				console.log('found', arr[i], arr[j], rem2);
				return [arr[i], arr[j], rem2]
			}
		}
	}
	return null
}

a = [1,2,4,6,8, 12]
findD(a, 8, 5);
for (var i = a.length-1; i >= 2; i--)
	console.log(findD(a, a[i], i+1))
