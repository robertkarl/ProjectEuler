# robert karl and zack gomez
# projecteuler.net, support functions for dealing with 
# primes, gcds, other stuff
# projecteuler.net, problem 214

# import psyco
# psyco.full()
from collections import deque
import math
import time

def prime_sieve(l):
    """
    slow!
    
    """
    curr_prime_index = 0
    current_prime = 2
    while current_prime < int(math.sqrt(l[-1])) + 1:
        i = curr_prime_index + 1
        while i < len(l):
            if l[i] % current_prime == 0 and l[i] != current_prime:
                l.remove(l[i])
            i += 1
        curr_prime_index += 1
        current_prime = l[curr_prime_index]
    return l
        

def merge(a,b):
    """
    O(n) merge for two sorted lists of length n

    performs mergesort on any two subscriptable objects
    implementing __lt__, __gt__, __eq__.
    
    @rtype: list
    """
    a_i = 0
    b_i = 0
    new = []
    while a_i < len(a) and b_i < len(b):
        if a[a_i] <= b[b_i]:
            #print "a[a_i]",a[a_i],"b[b_i]",b[b_i]
            #print "appending an a"
            new.append(a[a_i])
            a_i += 1
        else:
            #print "appending a b"
            new.append(b[b_i])
            b_i += 1
    while b_i < len(b):
        #print b_i,b
        new.append(b[b_i])
        b_i += 1
    while a_i < len(a):
        new.append(a[a_i])
        a_i += 1
    return new

class Factorer:
    """ a factorer that caches values. useful when calling factor() repeatedly.
    """
    def __init__(self):
        self.p = primes()
        self.i = 0
        self.cached_primes = 0
        self.plist = deque([])
        self.pset = set()
    def next_prime(self):
        if self.i < self.cached_primes:  
            p = self.plist[self.i]
        else:
            p = self.p.next()
            self.cache_prime(p)
        self.i += 1
        return p
    def cache_prime(self,n):
        self.plist.append(n)
        self.pset.add(n)
        self.cached_primes += 1
    def reset_primes(self):
        self.i = 0
    def factor(self,n):
        if self.is_prime(n):
            return [1,n]
        curr_prime = self.next_prime()
        curr = n
        factors = [1]
        while curr != 1:
            if curr % curr_prime == 0:
                factors.append(curr_prime)
                curr /= curr_prime
            else:
                curr_prime = self.next_prime()
        self.reset_primes()
        return factors

    def is_prime(self,n):
        """ 
        ###################################
        Check if n is prime. n must be at least 2.
        This function takes around n/6 time
        """
        if n in self.pset:
            return True
        if n < 2:
            raise Exception("is_prime() argument error")
        elif n < 4:
            return True
        elif n % 2 == 0:
            return False
        elif n < 9:
            # 5,7 
            return True
        elif n % 3 == 0:
            return False
        else:
            k = 5
            stop = int(math.sqrt(n))
            while k <= stop:
                if n % k == 0:
                    return False
                if n % (k + 2) == 0:
                    return False
                k += 6
            self.pset.add(n)
            return True


def prime_factors(n):
    """ there is a duplicate of this in math_pyrex_utils. not sure 
    what's fastest at this point.
    """
    if is_prime(n):
        return [1,n]
    ps = primes()
    curr_prime = ps.next()
    curr = n
    factors = [1]
    while curr != 1:
        if curr % curr_prime == 0:
            factors.append(curr_prime)
            curr /= curr_prime
        else:
            curr_prime = ps.next()
    return factors

def get_proper_divisors(n):
    divisors = []
    for i in range(1,n):
        if n % i == 0:
            divisors.append(i)
    return divisors
    


def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)


def gcd(a,b):
    """ this is where most of our time is spent
    """
    while b != 0:
        # a gets b, 
        # b gets a % b
        # repeat.
        t = b
        b = a % b
        a = t
    return a

def is_prime(n):
    """ Check if n is prime. n must be at least 2.
    This function takes around n/6 time
    """
    if n < 2:
        raise Exception("is_prime() argument error")
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        # 5,7 
        return True
    elif n % 3 == 0:
        return False
    else:
        k = 5
        stop = int(math.sqrt(n))
        while k <= stop:
            if n % k == 0:
                return False
            if n % (k + 2) == 0:
                return False
            k += 6
        return True

def binary_repr(n):
    """ thanks 2 internetz    """
    binary = lambda n: n>0 and [n&1]+binary(n>>1) or []
    l = binary(n)
    l.reverse()
    return ''.join([str(i) for i in l])

def euler_phi(n):
    """ calculate the number of integers less than n relatively prime
    to n.
    base case: If it's prime, our job is really, really easy.
    otherwise, we need to calculate the gcd n times, and that makes
    this function basically O(n^2).
    
    """
    if n < 1:
        raise Exception("euler_phi argument error: " + str(n))
    if n == 1:
        return 1
    if is_prime(n):
        return n - 1
    pfs = set(prime_factors(n))
    pfs.remove(1)
    return int(n * reduce(lambda x, y: x * y, [1 - 1.0/p for p in pfs]))


def get_totient_chain(n):
    answer = [n]
    next = n
    while next != 1:
        next = euler_phi(next)
        answer.append(next)
    return answer

def get_primes_list_of_length(num_primes):
    """ return this many primes
    """
    primes = []
    i = 2
    while len(primes) < num_primes:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

def primes():
    k = 2
    init = [2,3,5,7]
    for i in init:
        yield i
    while True:
        next = 6 * k - 1
        if is_prime(next):
            yield next
        if is_prime(next + 2):
            yield next + 2
        k += 1

def get_primes_list_less_than(max_n):
    """ return all primes less than max_n
    """
    primes = []
    i = 2
    while i < max_n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

RelPrimeCache = {}

def relativelyPrimeCount(a):
	if a % 2 == 0 and (a / 2) % 2 == 0 and RelPrimeCache.has_key(a / 2):
		ans = 2 * RelPrimeCache[a / 2]
		RelPrimeCache[a] = ans
		return ans
	f = Factorer()
	if (is_prime(a)):
		RelPrimeCache[a] = a - 1
		return a - 1
	fs = set(f.factor(a))
	fs.remove(1)
	count = 0
	for i in range(2, a):
		isRelativelyPrime = True
		for k in fs:
			if i % k == 0:
				isRelativelyPrime = False
				break
		# this number was relatively prime to a
		count += 1 if isRelativelyPrime else 0
	RelPrimeCache[a] = count + 1
	return count + 1

#
# 16
# 1 3 5 7 9 11 13 15
#
# 12
# 1 5 7 11
#
# 24
# 1 5 7 11 13 17 19 23 

def testRelativelyPrime():
	for (a, ans) in [(2, 1), (3, 2), (4, 2), (5, 4), (6, 2), (7, 6), (8, 4), (16, 8)]:
		assert relativelyPrimeCount(a) == ans

def startSearching(maxN):
	maxN = 1000000
	count = 0
	for i in range(2, maxN + 1):
		if i % 1000 == 0:
			print i
		count += relativelyPrimeCount(i)
	print count
	

if __name__ == "__main__":
	testRelativelyPrime()




