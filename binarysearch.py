
def binary_search_rec(x: int, arr, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == x:
        return mid
    elif arr[mid] < x:
        return binary_search_rec(x, arr, mid + 1, end)
    else:
        return binary_search_rec(x, arr, start, mid - 1)


data = [1, 1, 1, 2, 3, 3, 4, 5, 5, 6]
print(binary_search_rec(4, data, 0, len(data) - 1))
