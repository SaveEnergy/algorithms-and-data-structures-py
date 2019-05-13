
def binary_search_rec(x: int, a, pos, end):

    mid = (pos + end) // 2

    if pos > end:
        return -1
    elif a[mid] == x:
        return mid
    elif a[mid] < x:
        return binary_search_rec(x, a, mid + 1, end)
    else:
        return binary_search_rec(x, a, pos, mid - 1)


def binary_search(x: int, a):
    pos = 0
    end = len(a) - 1
    return binary_search_rec(x, a, pos, end)


print(binary_search(4, [1, 1, 2, 3, 4, 5]))
