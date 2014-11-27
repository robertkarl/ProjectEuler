

cache = {}

twobytwo = [[131, 673, 234, 103, 18], 
	[201, 96, 342, 965, 150],
	[630, 803, 746, 422, 111],
	[537, 699, 497, 121, 956],
	[805, 732, 524, 37, 331]]

fname = "p081_matrix.txt"

def cacheKey(i, j):
	return str(i) + "," + str(j)

def minPath(m, i, j):
	height = len(m)
	width = len(m[0])
	assert height > 0 and width > 0

	if (i < 0 or i >= height) or (j < 0 or j >= width):
		return -1

	k = cacheKey(i, j)
	if cache.has_key(k):
		return cache[k]

	l = minPath(m, i, j - 1)
	u = minPath(m, i - 1, j)
	curr = m[i][j]

	possibleValues = []
	if l > 0:
		possibleValues.append(l + curr)
	if u > 0:
		possibleValues.append(u + curr)
	if u < 0 and l < 0:
		assert i == 0 and j == 0
		possibleValues.append(curr) # base case
	cache[k] = min(possibleValues)
	return cache[k]


def readmatrix():
	m = []
	for line in open(fname):
		m.append([int(i) for i in line.split(",")])
	return m

if __name__ == "__main__":
	m = readmatrix()
	h = len(m)
	w = len(m[0])

	for i in range(h):
		for j in range(w):
			minPath(m, i, j)

	print minPath(m, h - 1, w - 1)


