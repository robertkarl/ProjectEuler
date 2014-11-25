import math

#
# key features: multiply two sum exprs
#


class expr(object):
	pass

class sum(expr):
	def __init__(self, addends):
		if not type(addends) == list:
			self.addends = [addends]
		self.addends = addends
	def __repr__(self):
		return "<sum of %s >" % str(self.addends)
	def evaluate(self):
		s = 0
		for i, val in enumerate(self.addends):
			s += val.evaluate()
		return s
	def __add__(self, other):
		return sum(self.addends + other.addends)

	def __mul__(self, other):
		l = []
		for i, val in enumerate(self.addends):
			for j, otherval in enumerate(other.addends):
				l.append(val * otherval)
		return sum(l)

	def simplified(self):
		a = self.addends
		ans = []
		v = value(0)
		for i, val in enumerate(a):
			if type(val) == value:
				v = v + val
		ans += filter(lambda x: type(x) != value, a)
		ans += [v]

		mults = filter(lambda x: type(x) == mult, ans)
		if len(mults) == 2 and mults[0].isOpposite(mults[1]):
			ans = filter(lambda x: type(x) != mult, ans)
		if len(ans) == 1:
			return ans[0]
		return sum(ans)





class value(expr):
	def __init__(self, value):
		self.value = value

	def __add__(self, other):
		if type(other) == value:
			return value(self.value + other.value)
		return sum([self, other])

	def __repr__(self):
		return "<value %s>" % str(self.value)

	def __mul__(self, other):
		if type(other) == value:
			return value(self.value * other.value)
		return mult([self, other])


	def evaluate(self):
		return self.value

class sqrt(value):
	def __mul__(self, other):
		if type(other) == sqrt and other.value == self.value:
			return value(self.value)
		return mult([self, other])
	def __repr__(self):
		return "<sqrt %d >" % self.value
	def __eq__(self, other):
		if type(other) == sqrt:
			return self.value == other.value
		return other == self
	def evaluate(self):
		return math.sqrt(self.value)



class div(expr):
	def __init__(self, top, bot):
		self.numer = top
		self.denom = bot

class mult(expr):
	def __init__(self, multiplicands):
		if not type(multiplicands) == list:
			self.multiplicands = [multiplicands]
		self.multiplicands = multiplicands

	def __repr__(self):
		return "<mult of %s >" % str(self.multiplicands)

	def evaluate(self):
		answer = 1
		for i, val in enumerate(self.multiplicands):
			answer *= val.evaluate()
		return answer
	def isOpposite(self, other):
		if len(self.multiplicands) == len(other.multiplicands) and len(self.multiplicands) == 2:
			isSqrt = lambda x: type(x) == sqrt
			isVal = lambda x: type(x) == value
			print "isOpposite(%s, %s)" % (str(self), str(other))
			sqrtMatches = filter(isSqrt, self.multiplicands)[0] == filter(isSqrt, other.multiplicands)[0]
			firstVal = filter(isVal, self.multiplicands)[0]
			otherVal = filter(isVal, other.multiplicands)[0]
			valMatches = firstVal.evaluate() == -1 * otherVal.evaluate()
			return sqrtMatches and valMatches

		return False


def testAdditionOfValues():
	a = value(3)
	b = value(-3)
	assert type(a + b) == value

def testMultiplicationOfSqrts():
	sqrt23 = sqrt(23)
	shouldBe23 = sqrt23 * sqrt23
	assert type(shouldBe23) == value and shouldBe23.evaluate() == 23

def testMultiplyingSums():
	s1 = sum([sqrt(23), value(4)])
	s2 = sum([sqrt(23), value(-4)])
	multiplied = s1  * s2
	print multiplied
	ans = multiplied.simplified()
	print ans
	assert type(ans) == value and ans.evaluate() == 7


if __name__ == "__main__":

	testAdditionOfValues()
	testMultiplicationOfSqrts()
	testMultiplyingSums()

