

test_num = 1000

numsum = 0
for i in range(test_num):
    if i % 3 == 0 or i % 5 == 0:
        numsum += i

print(numsum)