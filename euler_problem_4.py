
f = 0
dromes = []
for n in reversed(range(10, 1000)):
    for m in reversed(range(n, 1000)):
        prod = m * n
        prodstr = [int(d) for d in str(prod)]

        for i in range(0, int(len(prodstr) / 2)):
            if prodstr[i] != prodstr[len(prodstr) - i - 1]:
                break
            if i == int(len(prodstr) / 2)-1:
                dromes.append(prod)

print(max(dromes))