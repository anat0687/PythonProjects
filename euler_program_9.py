

a = 4
b = 3

solved = False

for a in range(1, 1001):
    if not solved:
        for b in range(1, 1001):
            c = (a**2 + b**2)**0.5
            if (a + b + c) == 1000:
                solved = True
                print(a * b * c)
                print(a, b, c)
                break
            b += 1
    a += 1
