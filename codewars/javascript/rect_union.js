function SegmentTree() {
	this.points = []
	this.isum = []
	this.counter = []
	this.buildTree = function (intervals) {
		for (var i = 0; i < intervals.length; i++) {
			this.points[2*i]   = intervals[i][0]
			this.points[2*i+1] = intervals[i][1]
		}
		this.points = this.points.sort()
		let k = 0
		for (i = 0; i < this.points.length; i++) {
			if (this.points[k] != this.points[i])
				this.points[++k] = this.points[i]
		}
	}

	this.insert_interval = function(interval) {
		this.insert_edge(1, 



	}

}

t = new SegmentTree()
