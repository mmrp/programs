function sum_3(arr, skip) {
	let n = arr.length
	d = arr[skip]
	for (let i = 0; i <= n-3; i++) {
		if (i == skip)
			continue
		a = arr[i]
		start = i+1
		end   = n-1
		while (start < end) {
			b = arr[start]
			c = arr[end]
			s = a + b + c
			if (s == d) {
				if (start != skip && end != skip) {
					console.log(a, b, c, d, start, end, skip, arr[skip])
					return true
				}
				if (b == arr[start+1])
					start++
				else
					end--
			}
			else
			if (s < d) 
				start++
			else
				end--
		}
	}
	return false
}

function findD(arr) {
	for (i = arr.length-1; i >= 0; i--)
		if (sum_3(arr, i))
			return arr[i]
	return null
}
arr = [-938,
  -821,
  -694,
  -626,
  -586,
  -509,
  -399,
  -387,
  -197,
  -47,
  71,
  73,
  131,
  215,
  235,
  370,
  522,
  610,
  667,
  694,
  729,
  874,
  932,
  976,
  996]
console.log(findD(arr))
/*
for i=0 to n-3 do
    a = S[i];
    start = i+1;
    end = n-1;
    while (start < end) do
       b = S[start]
       c = S[end];
       if (a+b+c == 0) then
          output a, b, c;
          // Continue search for all triplet combinations summing to zero.
          if (b == S[start + 1]) then
             start = start + 1;
          else
             end = end - 1;
       else if (a+b+c > 0) then
          end = end - 1;
       else
          start = start + 1;
       end
    end
 end
 */
