from math import sqrt
DEBUG = False

class SeqItem:
	def __init__(self, A, Y):
		self.A = A
		self.Y = Y
	def __eq__(self, other):
		asMatch = self.A == other.A 
		YsMatch = (self.Y - other.Y) < 1e-6
		return asMatch and YsMatch
	def __ne__(self, other):
		return not self == other
	def __repr__(self):
		return "<" + str(self.A) + "," + str(self.Y) + ">"

#
# input:  X
# output: A_i and Y s.t. X = 1/(a_i + Y)
#			A_i should be an integer and 0 < Y < 1
#
def get_seq(n):
	init = int(sqrt(n))
	s = []
	next = sqrt(n) - init
	while not seq_defined(s):
		curr = get_next(next)
		next = curr.Y
		s.append(curr)
		if DEBUG:
			print s
	return s[0 : len(s) / 2]

def get_next(X):
	inverted = 1.0 / X
	A =  int(inverted)
	Y = inverted - A
	return SeqItem(A, Y)

def seq_defined(s):
	if (len(s) > 10000):
		raise s
	if len(s) % 2 or len(s) == 0:
		return False
	seqlen = len(s) / 2
	for i in range(seqlen):
		if s[i] != s[i + seqlen]:
			return False
	return True

"""
#
#[<1,0.651387818866>, <1,0.535183758488>, <1,0.868517091821>, <1,0.151387818866>, <6,0.605551275464>, 
  <1,0.651387818865>, <1,0.53518375849>, <1,0.868517091816>, <1,0.151387818873>, <6,0.605551275154>, <1,0.651387819713>]
#
#
"""


def isSquare(i):
	s = int(sqrt(i))
	return i == s * s

if __name__ == '__main__':
	for n in range(2,1000):
		if isSquare(n): continue
		initialVal = int(sqrt(n))
		s = [i.A for i in get_seq(n)]
		print "sqrt " + str(n) + ": [" + str(initialVal) + ";" + str(s) + "], period = " + str(len(s))


