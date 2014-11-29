from Factorer import Factorer
import pickle

f = Factorer()
perms_fname = "/Users/androiddev/Documents/PE/totient_perms.pickle"

def persist(n):
    f = open(perms_fname)
    perms = pickle.load(f)
    f.close()
    perms.append(n)
    f_writing = open(perms_fname, 'w')
    pickle.dump(list(set(perms)), f_writing)
    f_writing.close()

def get_pickled_perms():
    return sorted(set(pickle.load(open(perms_fname))))

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

maxN = int(1e7)

def continue_searching():
    vals = get_pickled_perms()
    start = max(vals)
    print "continuing to find permutations from %d" % start
    for i in xrange(start + 1, maxN):
        phi = f.phi(i)
        if is_permutation(i, phi):
            print "phi(%d) = %d" % (i, phi)
            persist(i)
            r = float(i)/f.phi(i)
            print "ratio is %f" % r

if __name__ == "__main__":
    continue_searching()