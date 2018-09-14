#!/usr/bin/python

def parse_molecule(formula):
	dct = {}

	def isdigit(c):
		if not c:
			return False
		return True if c >= '0' and c <= '9' else False

	def isupper(c):
		if not c:
			return False
		return c.isupper()

	def islower(c):
		if not c:
			return False
		return c.islower()

	def digit(f):
		c = 0
		while isdigit(f[c]):
			c += 1
		return int(f[:c]), c

	def add(d, c, v):
		if c not in d:
			d[c] = v
		else:
			d[c] += v

	cur = ''
	f = formula
	while f:
		if isdigit(f[0]):
			v, s = digit(f)
			f = f[s+1:]
			add(dct, cur, v)
			cur = ''

		elif isupper(f[0]):
			if cur: 
				add(dct, cur, 1)
				cur = ''

			cur += f[0]
			f = f[1:]
			if islower(f[0]):
				cur += f[0]
				f = f[1:]


fremySalt = 'K4[ON(SO3)2]2'
parse_molecule(fremySalt)         

