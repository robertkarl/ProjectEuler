
#
# these numbers are wrong!
# 464, 465, 315, 313, 312, 314
#

def make_line(pt1, pt2):
	x1 = pt1[0]
	x2 = pt2[0]
	y1 = pt1[1]
	y2 = pt2[1]
	if x2 - x1 == 0:
		return (None, x1)
	m = (y2 - y1) / (x2 - x1)
	b = y2 - m * x2
	return (m, b)

def strictly_above(line, x, y):
	m = line[0]
	b = line[1]
	return m * x + b < y

def is_on_line(line, pt):
	assert len(pt) == 2
	x = pt[0]
	y = pt[1]
	if line[0] == None:
		xval = line[1]
		return x == xval
	m = line[0]
	b = line[1]
	return m * x + b == y

def same_side(line, pt1, pt2):
	if line[0] == None:
		xval = line[1]
		x1 = pt1[0]
		x2 = pt2[0]
		if x1 == xval or x2 == xval:
			print "short circuiting for line %s" % str(line)
			return True
		theVal = not (x1 > xval and x2 < xval) and not (x1 < xval and x2 > xval)
		return theVal
	if is_on_line(line, pt1) or is_on_line(line, pt2):
		return True
	first = strictly_above(line, pt1[0], pt1[1])
	sec = strictly_above(line, pt2[0], pt2[1])
	print "line is %s x + %s" % (str(line[0]), str(line[1]))
	print "%s is above? %d" % (str(pt1), first)
	print "%s is above? %d" % (str(pt2), sec)

	return first == sec

def containsOrigin(points):
	A = [points[0], points[1]]
	B = [points[2], points[3]]
	C = [points[4], points[5]]
	print A, B, C
	O = [0, 0]

	AC = make_line(A, C)
	AB = make_line(A, B)
	BC = make_line(B, C)

	cond_a = same_side(BC, A, O)
	cond_b = same_side(AC, O, B)
	cond_c = same_side(AB, C, O)
	print "Triangle conditions?", (cond_a, cond_b, cond_c)

	return cond_c and cond_b and cond_a


def test_triangles():
	t1 = [0, 0, 1, 0, 0, 1]
	t2 = [1, 0, 1, 1, 2, 0]
	assert containsOrigin(t1)
	assert not containsOrigin(t2)

	t3 = [0, 0, -1, 0, 0, 1]
	assert containsOrigin(t3)

	t4 = [0, 0, 1, 0, 0, -1]
	assert containsOrigin(t4)

	coversOrigin = [0, 1, 1, -1, -1, -1]
	assert containsOrigin(coversOrigin)

	throughOrigin = [-1, 1, -1, -1, 1, -1]
	assert containsOrigin(throughOrigin)

	throughOrigin2 = [1, 1, 1, -1, -1, 1]
	assert containsOrigin(throughOrigin2)

	throughOriginVertical = [0, 1, 0, -1, 1, 0]
	assert containsOrigin(throughOriginVertical)

	throughOriginHorizontal = [-1, 0, 1, 0, -1, 0]
	assert containsOrigin(throughOriginHorizontal)

	throughOriginDiagonal = [-1, -1, 1, 1, 1, -1]
	assert containsOrigin(throughOriginDiagonal)

def test_same_side():
	flatline = [0, 0]
	vertLine = [None, 0]

	r = (1, 0)
	l = (-1, 0)
	u = (0, 1)
	d = (0, -1)

	assert same_side(flatline, l, r)
	assert same_side(flatline, l, u)
	assert same_side(flatline, l, d)
	assert not same_side(flatline, u, d)
	assert not same_side(flatline, d, u)

	# vertical line through origin
	assert not same_side(vertLine, l, r)
	assert not same_side(vertLine, r, l)
	assert same_side(vertLine, u, l)
	assert same_side(vertLine, u, r)

if __name__ == "__main__":
	test_same_side()	
	test_triangles()

def runTestFile():
	fname = "p102_triangles.txt"
	ans = 0
	for line in open(fname):
		t = [int(i) for i in line.split(",")]
		c = containsOrigin(t)

		if c: ans += 1
	print ans
