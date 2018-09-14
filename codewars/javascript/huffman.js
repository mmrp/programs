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

function  huffman(freq) {
	fsum = freq.reduce((r, v) => v[1] + r, 0)
	this.ratio = freq.map((v) => [v[1]/fsum, v[0]]).sort((a, b) => a[0] - b[0])
	this.table = {}

	q = new minpq()
	for (let i = 0; i < this.ratio.length; i++) {
		q.push({'name':this.ratio[i][1], 'value': this.ratio[i][0]})
	}


	while (q.length() > 1) {
		a = q.pop()
		b = q.pop()
		q.push({'name':a.name + b.name, 'value':a.value + b.value, 'left': a, 'right':b})
	}

	this.findmap = function (node, code) 
	{
		if (node == undefined) return

		this.findmap(node.left, code + '0')
		this.findmap(node.right, code + '1')
		if (node.left == undefined && node.right == undefined) 
			this.table[node.name] = code
		
	}

	this.encode = function(s) 
	{
		console.log(this.table)
		return s.split("").map((v) => this.table[v]).join("")
	}

	this.decode = function(s)
	{
		let res = ''
		let i = 0
		while (i < s.length) {
			let node = this.head;
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
	this.head = q.pop()
	this.findmap(this.head, '')
	
}

a = new huffman([['a', 5], ['b', 9], ['c', 12], ['d', 13], ['e', 16], ['f', 45]])
a = new huffman([ [ '3', 2 ], [ '7', 2 ], [ 'p', 1 ], [ 'r', 1 ], [ 'b', 1 ], [ 'n', 1 ], [ 'f', 3 ], [ 't', 1 ], [ 'h', 1 ], [ 'x', 1 ], [ 'l', 1 ], [ 'u', 1 ], [ 'e', 1 ], [ 'c', 1 ], [ 'd', 1 ], [ 'i', 1 ] ])
console.log(a.decode('1101010000111110111011001111101001010011000111100011101111001010010011011000101'))
/*
b = new minpq()
for (let i = 0; i < 100; i++) 
	b.push(parseInt(Math.random() * 100))
//b.push(7)
f = b.pop()
while ((v = b.pop()) != undefined && v <= f); 
console.log(b.pop())*/
