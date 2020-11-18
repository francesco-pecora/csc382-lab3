import random


def quickSort(array, start, end, steps = 0):
    if start >= end:
        return steps

    steps += 1

    p, steps = partition(array, start, end, steps)
    steps = quickSort(array, start, p-1, steps)
    steps = quickSort(array, p+1, end, steps)

    steps += 3

    return steps


def partition(array, start, end, steps):
    pivot = array[start]
    low = start + 1
    high = end
    steps += 3

    while True:

        while low <= high and array[high] >= pivot:
            high = high - 1
            steps += 3
        while low <= high and array[low] <= pivot:
            low = low + 1
            steps += 3
        if low <= high:
            array[low], array[high] = array[high], array[low]
            steps += 2
        else:
            steps += 1
            break

    array[start], array[high] = array[high], array[start]
    steps += 1

    return high, steps


if __name__ == '__main__':
    n = 100
    a = [random.randint(1, n) for _ in range(1, n + 1)]
    # a = [x for x in range(0, n - 1)]
    steps = quickSort(a, 0, len(a) - 1)
    print(a, steps)