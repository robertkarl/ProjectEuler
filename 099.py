
fname = "p099_base_exp.txt"



if __name__ == "__main__":
	x = []
	k = 0
	for line in open(fname):
		(base, exponent) = [int(i) for i in line.split(",")]
		x.append(base ** exponent)
		print "appended %d or %s" % (k, line.strip())
		k += 1
	largest_index = 0
	prev = 0
	for i in range(len(x)):
		if x[i] > prev:
			largest_index = i
			prev = x[i]
	print largest_index
