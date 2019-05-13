

def fac(n: int):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fac_rec(n: int):
    if n == 0:
        return 1
    else:
        return n * fac_rec(n - 1)


print(fac_rec(2))
print(fac(4))
