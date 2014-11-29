from Factorer import Factorer
import pickle

f = Factorer()
perms_fname = "totient_perms.pickle"

def persist(n):
    perms = pickle.load(open(perms_fname))
    perms.append(n)
    pickle.dump(list(set(perms)), open(perms_fname, 'w'))

def get_pickled_perms():
    return sorted(set(pickle.load(open(perms_fname))))

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

l = [(0,0)]
curr = 0
max = 1000*1000
print "running euler69 phi with max ",max

for i in range(2,max):
    phi = f.phi(i)
    if is_permutation(i, phi):
        print "phi(%d) = %d" % (i, phi)
        persist(i)
        r = float(i)/f.phi(i)
        print "ratio is %f" % r

print "solutions, in increasing order. or something"
for i in l:
    print i
