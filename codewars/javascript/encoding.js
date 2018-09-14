function Buffer(subject, encoding, offset) {
  if (!(this instanceof Buffer)) {
    return new Buffer(subject, encoding, offset);
  }

  var type;

  // Are we slicing?
  if (typeof offset === 'number') {
    if (!Buffer.isBuffer(subject)) {
      throw new TypeError('First argument must be a Buffer when slicing');
    }

    this.length = +encoding > 0 ? Math.ceil(encoding) : 0;
    this.parent = subject.parent ? subject.parent : subject;
    this.offset = offset;
  } else {
    // Find the length
    switch (type = typeof subject) {
      case 'number':
        this.length = +subject > 0 ? Math.ceil(subject) : 0;
        break;

      case 'string':
        this.length = Buffer.byteLength(subject, encoding);
        break;

      case 'object': // Assume object is array-ish
        this.length = +subject.length > 0 ? Math.ceil(subject.length) : 0;
        break;

      default:
        throw new TypeError('First argument needs to be a number, ' +
                            'array or string.');
    }

    if (this.length > Buffer.poolSize) {
      // Big buffer, just alloc one.
      this.parent = new SlowBuffer(this.length);
      this.offset = 0;

    } else if (this.length > 0) {
      // Small buffer.
      if (!pool || pool.length - pool.used < this.length) allocPool();
      this.parent = pool;
      this.offset = pool.used;
      // Align on 8 byte boundary to avoid alignment issues on ARM.
      pool.used = (pool.used + this.length + 7) & ~7;

    } else {
      // Zero-length buffer
      this.parent = zeroBuffer;
      this.offset = 0;
    }

    // optimize by branching logic for new allocations
    if (typeof subject !== 'number') {
      if (type === 'string') {
        // We are a string
        this.length = this.write(subject, 0, encoding);
      // if subject is buffer then use built-in copy method
      } else if (Buffer.isBuffer(subject)) {
        if (subject.parent)
          subject.parent.copy(this.parent,
                              this.offset,
                              subject.offset,
                              this.length + subject.offset);
        else
          subject.copy(this.parent, this.offset, 0, this.length);
      } else if (isArrayIsh(subject)) {
        for (var i = 0; i < this.length; i++)
          this.parent[i + this.offset] = subject[i];
      }
    }
  }

  SlowBuffer.makeFastBuffer(this.parent, this, this.offset, this.length);
}

a = new Buffer('input', 'base64') 
console.log(a)
