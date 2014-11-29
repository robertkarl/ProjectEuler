# 9878831 has ratio of 1.00006559911
# 8202863 has ratio of 1.0000274302
# 7609198 has ratio of 1.00002720466 with 5 factors
from Factorer import Factorer
f = Factorer()
f.factor(100003 * 2) # populate primes table
primes = f.plist


def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

best_ratio = 5
best_val = -1

# n (1 - 1/p1) (1 - 1/p2)
for p1 in primes:
	for p2 in primes:
		if p1 * p2 > 1e7: break
		for p3 in primes:
			if p1 * p2 * p3 > 1e7: break
			for p4 in primes:
				if p1 * p2 * p3 * p4 > 1e7: break
				for p5 in primes:
					semiprime = p1 * p2 * p3 * p4 * p5
					if semiprime > 1e7:
						break
					phi = semiprime - p1 - p2 - p3 - p4 - p5 + 1
					r = float(semiprime) / phi
					if is_permutation(phi, semiprime) and r < best_ratio:
						best_ratio = r
						best_val = semiprime
						print p1, p2, semiprime, phi, best_ratio




