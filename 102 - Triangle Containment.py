
#
# these numbers are wrong!
# 464, 465, 315, 313
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

def above(line, x, y):
	m = line[0]
	b = line[1]
	return m * x + b <= y

def same_side(line, pt1, pt2):
	print "line",line,"points:", pt1, pt2
	if line[0] == None:
		xval = pt1[1]
		x1 = pt1[0]
		x2 = pt2[0]
		theVal = not (x1 > xval and x2 < xval) or (x1 < xval and x2 > xval)
		print pt1, pt2, "same side of line:", line, "?", theVal
		return theVal
	first = above(line, pt1[0], pt1[1])
	sec = above(line, pt2[0], pt2[1])
	print first, sec

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
	cond_b = same_side(AC, O, B)
	print "getting condition C" 
	cond_c = same_side(AB, C, O)

	print "conditions %d, %d, %d" % (cond_a, cond_b, cond_c)

	return cond_c and cond_b and cond_a


def test_triangles():
	points = [0, 0, 1, 0, 0, 1]
	assert containsOrigin(points)


test_triangles()
fname = "p102_triangles.txt"
ans = 0
for line in open(fname):
	t = [int(i) for i in line.split(",")]
	c = containsOrigin(t)
	print t, c
	if c: ans += 1
print ans
