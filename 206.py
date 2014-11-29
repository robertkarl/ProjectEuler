"""
For each number between sqrt(102e16) --> sqrt(192e16):
	square it and see if it has the right form
"""
from math import sqrt
s = int(sqrt(102e16))
e = int(sqrt(193e16))

for i in xrange(s, e + 1):
	if i % 1000000 == 0:
		print "checking i %d or %s" % (i, str(i * i)[::2])
		print "i * i = %s" % str(i * i)
	if i * i % 10 == 0:
		s = str(i * i)[::2]
		ans = "1234567890"
		assert len(ans) == len(s) and type(s) == type(ans)
		if s == "1234567890":
			print i
			break


