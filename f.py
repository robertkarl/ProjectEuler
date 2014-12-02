import sqlite3
from Factorer import Factorer

conn = None
f = Factorer()

def getConnection():
    global conn
    if not conn:
        print "initializing db"
        conn = sqlite3.connect('factors.db')
    return conn

def getCursor():
    return getConnection().cursor()

def resetTable():
    c = getCursor()
    c.execute("drop table if exists Factors")
    c.execute("create table Factors (n int, f int, p int) ")
    c.execute("insert into factors values (2, 2, 1)")
    getConnection().commit()

def getLargestFactoredInteger():
    c = getCursor()
    return c.execute("select * from factors order by n desc limit 1").fetchone()[0]

def resetFactorsUntil(maxN):
    f = Factorer()
    n = getLargestFactoredInteger() + 1
    c = getCursor()
    while n <= maxN:
        factors = f.factor(n)
        factors.pop(0)
        if n % 5000 == 0:
            print "factors(%d) = %s" % (n, str(factors))
        if (f.is_prime(n)):
            c.execute("insert into factors values (?, ?, 1)", (n, n))
        else:
            for i in factors:
                c.execute("insert into factors values (?, ?, 0)", (n, i))
        n += 1
    getConnection().commit()

def factor(n):
    if n < 1:
        raise "Can't factor %d" % n
    factors = [i[1] for i in getCursor().execute("select * from factors where n = %d" % n).fetchall()]
    if not len(factors):
        return f.factor(n)
    return factors

if __name__ == "__main__":
    c = getCursor()


