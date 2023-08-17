def mndel(a):
    for x in range(2, a):
        if a % x == 0:
            return x
    return 0


def mxdel(b):
    for y in range(b-1, 2, -1):
        if b % y == 0:
            return y
    return 0


z = 0
c = 850001
while z < 6:
    f = mxdel(c) - mndel(c)
    if (f != 0) and (f % 5 == 0):
        print(c, f)
        z += 1
    c += 1
