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
	return (m * x + b) < y

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
	if is_on_line(line, pt1) or is_on_line(line, pt2):
		return True
	if line[0] == None:
		xval = line[1]
		x1 = pt1[0]
		x2 = pt2[0]
		if x1 == xval or x2 == xval:
			return True
		theVal = (not (x1 > xval and x2 < xval)) and (not (x1 < xval and x2 > xval))
		return theVal
	first = strictly_above(line, pt1[0], pt1[1])
	sec = strictly_above(line, pt2[0], pt2[1])
	return first == sec

def containsOrigin(points):
	A = [points[0], points[1]]
	B = [points[2], points[3]]
	C = [points[4], points[5]]
	O = [0, 0]

	AC = make_line(A, C)
	AB = make_line(A, B)
	BC = make_line(B, C)

	cond_a = same_side(BC, A, O)
	cond_b = same_side(AC, B, O)
	cond_c = same_side(AB, C, O)

	return cond_c and cond_b and cond_a


def test_triangles():
	firstExample = [-340, 495, -153, -910, 835, -947]
	assert containsOrigin(firstExample)
	secondExample = [-175, 41, -421, -714, 574, -645]
	assert not containsOrigin(secondExample)

	t1 = [0, 0, 1, 0, 0, 1]
	t2 = [1, 0, 1, 1, 2, 0]
	assert containsOrigin(t1)
	assert not containsOrigin(t2)

	t3 = [0, 0, -1, 0, 0, 1]
	assert containsOrigin(t3)

	t4 = [0, 0, 1, 0, 0, -1]
	assert containsOrigin(t4)
	t5 = [-1, 1, -1, 0, 0, 0]
	assert containsOrigin(t5)

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

	endsAtOrigin = [-1, 0, 0, 0, -1, -1]
	assert containsOrigin(endsAtOrigin)

	originOnVertLine = [0, 1, 0, -1, 1, 0]
	assert containsOrigin(originOnVertLine)

	print "containment passed"

r = (1, 0)
l = (-1, 0)
u = (0, 1)
d = (0, -1)


def test_same_side():
	flatline = [0, 0]
	vertLine = [None, 0]

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
	assert same_side(vertLine, l, u)
	assert same_side(vertLine, r, u)
	print "same_side passed"

def test_make_line():
	# TODO verify
	for pt1, pt2, line in [[u, d, (None, 0)],
			[l, r, (0, 0)],
			[(1, 0), (1, 1), (None, 1)]]:
		assert make_line(pt1, pt2) == line
	print "make_line passed"

def test_is_online():
	vert = (None, 1)
	assert is_on_line(vert, (1, 0))
	assert not is_on_line(vert, (0, 0))
	assert not is_on_line(vert, (2, 0))

	horz = (0, 1)
	assert is_on_line(horz, (0, 1))
	assert not is_on_line(horz, (0, -1))
	assert not is_on_line(horz, (0, 2))

	l1 = (1, 0)
	assert is_on_line(l1, (0, 0))
	assert not is_on_line(l1, (-1, 1))
	assert not is_on_line(l1, (1, -1))
	print "is_on_line passed"

X = (-175, 41)
Y = (-421, -714)
Z = (574, -645)

if __name__ == "__main__":
	test_same_side()	
	test_triangles()
	test_make_line()
	test_is_online()

def runTestFile():
	fname = "p102_triangles.txt"
	ans = 0
	totalLines = 0
	for line in open(fname):
		t = [int(i) for i in line.split(",")]
		if containsOrigin(t):
			ans += 1
		totalLines += 1
	assert totalLines == 1000
	print ans
