
f = 1
ans = 10
a = 1
while f == 1:
    for i in reversed(range(1, 21)):
        if ans % i != 0:
            ans += 1
            break
        if i == 1:
            f = 0
            print("here")
            break


print(ans)
