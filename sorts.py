import random
import math

ARRAYSIZE = 1000


def swap(array, x, y):
    tmp = array[x]
    array[x] = array[y]
    array[y] = tmp


def compare_lt(x, y):
    return x < y


def bubblesort(array, start, stop):
    # Bubblesort it... it's the only way to be sure

    for _ in range(math.ceil((len(array)))):
        for x in range(len(array) - 1):
            if compare_lt(array[x + 1], array[x]):
                swap(array, x, x + 1)


def quicksort(array, start, stop):
    if stop - start < 2:
        return True

    larger_index = stop - 2
    smaller_index = start
    # the "whole" starts where the pivot does
    pivot = array[stop - 1]
    hole = stop - 1

    while larger_index + 1 > smaller_index:
        if compare_lt(pivot, array[larger_index]):
            # good case, this is the right side
            # just shift the whole and continue!
            array[hole] = array[larger_index]
            larger_index -= 1
            hole -= 1
        else:
            # gotta put it on the other side
            swap(array, larger_index, smaller_index)
            smaller_index += 1

    array[hole] = pivot

    quicksort(array, start, hole)
    quicksort(array, hole + 1, stop)


def test_sort(sortfn):
    random.seed('ladyred')
    array = [random.randrange(ARRAYSIZE) for x in range(ARRAYSIZE)]
    sortfn(array, 0, len(array))
    print(array)
    for x, y in zip(array, array[1:]):
        assert x <= y, f"{x} !<= {y}"


def main():
    test_sort(quicksort)
    test_sort(bubblesort)


if __name__ == '__main__':
    main()
