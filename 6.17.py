a = [int(x) for x in open('17var6.txt')]
k = 0
mnmod = 20005
for i in range(len(a)-1):
    if (a[i] % 10 == 7) and (a[i+1] % 10 == 7):
        k += 1
        if abs(a[i] - a[i+1]) < mnmod:
            mnmod = abs(a[i] - a[i+1])
print(k, mnmod)
