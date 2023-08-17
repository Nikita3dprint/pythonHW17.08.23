k = 0
for x in range(5):
    for y in range(5):
        for z in range(5):
            if (x > y) and (y > z):
                k += 1
print(k)
