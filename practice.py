def facto(n):
    if n < 2:
        return n
    else:
        return n * facto(n-1)


def facto2(n):
    if n == 1:
        return n
    else:
        res = n
        for i in range(n-1, 0, -1):
            res *= i
        return res

a = 1

print(facto(a))
print(facto2(a))