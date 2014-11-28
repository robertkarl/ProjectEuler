# robert karl and zack gomez
# projecteuler.net, support functions for dealing with 
# primes, gcds, other stuff

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
        self.p = self.primes()
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
    def phi(self, n):
        """ calculate the number of integers less than n relatively prime
        to n.
        """
        if n < 1:
            raise Exception("euler_phi argument error: " + str(n))
        if n == 1:
            return 1
        if self.is_prime(n):
            return n - 1
        pfs = set(self.factor(n))
        pfs.remove(1)

        prod = n
        for currPrime in pfs:
            prod -= prod / currPrime
        return prod

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
    def primes(self):
        k = 2
        init = [2,3,5,7]
        for i in init:
            yield i
        while True:
            next = 6 * k - 1
            if self.is_prime(next):
                yield next
            if self.is_prime(next + 2):
                yield next + 2
            k += 1

def get_proper_divisors(n):
    divisors = []
    for i in range(1,n):
        if n % i == 0:
            divisors.append(i)
    return divisors

def gcd(a,b):
    while b != 0:
        # a gets b, 
        # b gets a % b
        # repeat.
        t = b
        b = a % b
        a = t
    return a

def countFractions(maxN):
    """
    returned 303963522857 for 1000000.
    303,963,522,857
    8 --> 21
    10000  --> 30,397,349
    100000 --> 3,039,648,680
    200000 --> 12,158,598,917
    """
    f = Factorer()
    count = 0
    for i in range(2, maxN + 1):
        if i % 10000 == 0:
            print i
        count += f.phi(i)
    print count
    
def testFactoring():
    f = Factorer()
    for i in [2,3,5,7,11,13,17]:
        assert f.is_prime(i)
    for i in [4,6,8,9,10,12,14,15,16]:
        assert not f.is_prime(i)
    assert set(f.factor(2 * 3 * 5 * 7)) == set([1, 2, 3, 5, 7])
    assert set(f.factor(2 * 3 * 2 * 3 * 5 * 7)) == set([1, 2, 3, 5, 7])

def testPhi():
    f = Factorer()
    for (a, ans) in [(2, 1), (3, 2), (4, 2), (5, 4), (6, 2), (7, 6), (8, 4), (16, 8)]:
        assert f.phi(a) == ans
    f = Factorer()
    assert f.phi(1000000) == 400000

if __name__ == "__main__":
    testFactoring()
    testPhi()


