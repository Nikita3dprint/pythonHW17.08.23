x = 3 ** 2020 - 3 ** 1020 + 9 ** 800 - 81
k = 0
while x > 0:
    if x % 10 == 2:
        k += 1
    x = x // 10
print(k)
