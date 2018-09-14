function minpq() {
	this.arr = [{}]
	this.N = 0
	
	this.length = function() { return this.N; }

	this.greater = function(p, q) 
	{ 
		return this.arr[p].value > this.arr[q].value; 
	}

	
	this.exch = function(p, q)
	{ 
		let t = this.arr[p]; 
		this.arr[p] = this.arr[q]; 
		this.arr[q] = t; 
	}

	this.swim_up = function(k) 
	{
		while (k > 1 && this.greater(~~(k/2), k)) {
			this.exch(~~(k/2), k);
			k = ~~(k/2)
		}
	}

	this.push = function(e) 
	{
		this.arr[++this.N] = e
		this.swim_up(this.N)
	}

	this.sink = function(k)
	{
		let N = this.N 
		while (2*k <= N) {
			let j = 2*k
			if (j+1 <= N && this.greater(j, j+1)) j++
			if (!this.greater(k, j)) break
			this.exch(k, j)
			k = j
		}
	}

	this.pop = function ()
	{
		if (this.N == 0)  return undefined

		let top = this.arr[1]
		this.arr[1] = this.arr[this.N]
		this.N--
		this.sink(1)
		return top

	}


}

function  huffman() {
  this.frequencies = function (s) 
  {
    let tbl = {}
    for (let i = 0; i < s.length; i++)
      tbl[s[i]] = (tbl[s[i]] || 0) + 1
    let freq = []
    for (e in tbl) freq.push([e, tbl[e]])
    return freq
   }
	

	this.findmap = function (node, code, table) 
	{
		console.log(typeof(table))
		if (node == undefined) return

		this.findmap(node.left, code + '0', table)
		this.findmap(node.right, code + '1', table)
		if (node.left == undefined && node.right == undefined) 
			table[node.name] = code
		
	}
	this.preprocess = function(freq)
	{
		fsum = freq.reduce((r, v) => v[1] + r, 0)
		ratio = freq.map((v) => [v[1]/fsum, v[0]]).sort((a, b) => a[0] - b[0])
	
		let q = new minpq()
		for (let i = 0; i < ratio.length; i++) {
			q.push({'name':ratio[i][1], 'value': ratio[i][0]})
		}
		while (q.length() > 1) {
			let a = q.pop()
			let b = q.pop()
			q.push({'name':a.name + b.name, 'value':a.value + b.value, 'left': a, 'right':b})
		}
		return q
  
	}
	this.encode = function(freq, s) 
	{
	    let q = this.preprocess(freq) 
		let table = {}
	    this.findmap(q.pop(), '', table)
		console.log(table)
		return s.split("").map((v) => table[v]).join("")
	}

	this.decode = function(freq, s)
	{
		let q = this.preprocess(freq) 
		let head = q.pop()
		let res = ''
		let i = 0
		while (i < s.length) {
			let node = head;
			while (!(node.left == undefined && node.right == undefined)) {
				if (s[i++] == '0')
					node = node.left
				else
					node = node.right
			}
			res += node.name
		}
		return res
	}
}

h = new huffman()
function frequencies(s) {return h.frequencies(s);}
function encode(fs, s) { return h.encode(fs, s); }
function decode(fs, s) { return h.decode(fs, s); }

const s = "aaaabcc";
const fs = frequencies(s);
console.log(fs)
console.log([...fs].sort(), [ ["a",4], ["b",1], ["c",2] ])
console.log( encode( fs, s ).length, 10)

const fs1 = [ [ '3', 2 ], [ '7', 2 ], [ 'p', 1 ], [ 'r', 1 ], [ 'b', 1 ], [ 'n', 1 ], [ 'f', 3 ], [ 't', 1 ], [ 'h', 1 ], [ 'x', 1 ], [ 'l', 1 ], [ 'u', 1 ], [ 'e', 1 ], [ 'c', 1 ], [ 'd', 1 ], [ 'i', 1 ] ]
console.log(decode(fs1, '1101010000111110111011001111101001010011000111100011101111001010010011011000101'))
