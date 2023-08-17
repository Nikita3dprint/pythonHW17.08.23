for n in range(200):
    n -= n % 4
    b = bin(n)[2:]
    b += str(b.count('1') % 2)
    b += str(b.count('1') % 2)
    r = int(b, 2)
    if r > 100:
        print(r)
        break
