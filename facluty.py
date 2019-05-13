

def fac(n: int):
    i = 0
    result = 1
    while i < n:
        i += 1
        result *= i
    return result


def fac_rec(n: int):

    # wird n+1 mal aufgerufen

    if n == 0:
        return 1
    else:
        return n * fac_rec(n - 1)


print(fac_rec(4))
