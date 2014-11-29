from math_rk import Factorer

f = Factorer()

l = [(0,0)]
curr = 0
max = 1000*1000
print "running euler69 phi with max ",max
for i in range(2,max):
    if i % 1000 == 0:
        print i
    n = float(i)/f.euler_phi(i)
    if n > l[curr][1]:
        l.append((i,n))
        curr += 1

print "solutions, in increasing order. or something"
for i in l:
    print i