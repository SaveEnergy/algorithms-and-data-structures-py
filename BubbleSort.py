import random

rand_data = [random.randint(0, 100) for i in range(10)]


def swap(x: int, array: list):
    array[x], array[x+1] = array[x+1], array[x]


def bubble_sort(array: list):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                swap(j, array)
    return array


def bubble_sort_rec(array: list, n: int):
    if n == 1:
        return array
    else:
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                swap(i, array)
                bubble_sort_rec(array, n - 1)
        return array


print("Random Liste:")
print(rand_data)
print("\nBubblesort rekursiv:")
print(bubble_sort_rec(list(rand_data), len(rand_data)))
print("\nBubblesort iterativ:")
print(bubble_sort(list(rand_data)))
