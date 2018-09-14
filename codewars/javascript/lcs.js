function lcs(a, b) {
//	console.log(a, b)
	let table = new Array(a.length+1)	
	for (let i = 0; i < table.length; i++) {
		table[i] = new Array(b.length+1)
		table[i][0] = 0
	}

	for (let j = 0; j < b.length+1; j++)
		table[0][j] = 0
	for (i = 1; i <= a.length; i++) { 
		for (j = 1; j <= b.length; j++) {
			if (a[i-1] == b[j-1])
				table[i][j] = table[i-1][j-1] + 1
			else
				table[i][j] = Math.max(Math.max(table[i-1][j], table[i][j-1]), table[i-1][j-1])
		}
	}
	i--, j--;
//	console.log(table)
//	console.log(table[i][j])
	let str = ""
	while (i >= 1 && j >= 1) {
		if (a[i-1] == b[j-1]) {
			str += a[i-1]
			i--, j--
		}
		else
		if (table[i][j] == table[i][j-1]) { //moving across row
			str += b[j-1]
			j--
		}
		else {								//moving across col
			str += a[i-1]
			i--
		}
//		console.log(str, i, j)
	}
	while (i > 0) {
		str += a[i-1]
		i--
	}
	while (j > 0) {
		str += a[j-1]
		j--
	}
	
	return str.split("").reverse().join("")
}

function shortest(sequences){
	let s = sequences[0]
	let o; 
	for (let i = 1; i < sequences.length; i++) {
		o = s
		s = lcs(s, sequences[i])
//		console.log(o, sequences[i], s)
	}
	return s
}


var superseq;
function permute(a, s, n, sequences) {
	if (s == n) {
		let arr = []
		for (let k = 0; k < n; k++)
			arr.push(sequences[a[k]])
		let tmp = shortest(arr)
		//console.log('shortest', tmp, superseq.length)
		if (superseq.length > tmp.length) 
			superseq = tmp.slice(0)
		return
	}
	for (let j = s; j < n; j++) {
		let t = a[s]
		a[s] = a[j]
		a[j] = t
		permute(a, s+1, n, sequences)
		t = a[s]
		a[s] = a[j]
		a[j] = t
	}

}


function shortestCommonSupersequence(sequences) {
	superseq = "0".repeat(100)
	a = new Array(sequences.length)
	for (let i = 0; i < a.length; i++)
		a[i] = i
	permute(a, 0, a.length, sequences)
//	console.log('final', max)
	return superseq
}


//console.log(shortestCommonSupersequence(['shor', 'hort',  'rtes', 'test']))
console.log(shortestCommonSupersequence(['hello', 'world'])) //,  'rtes', 'test']))
console.log(shortestCommonSupersequence(['ABRAC', 'ACADA', 'ADABR', 'DABRA', 'RACAD'])) //,  'rtes', 'test']))
console.log(shortestCommonSupersequence(['abcde', 'dek', 'cdejd'])) //,  'rtes', 'test']))

//console.log(lcs("HEMLJLOE", "ELOE"))
//console.log(lcs("AGGTAB", "GXTXAYB"))
//console.log(lcs("HELLO", "GEEK"))
