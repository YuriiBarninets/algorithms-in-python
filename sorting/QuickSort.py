import random
"""
O(N) : N * log N
Worst case : N^2

Pos :
 * Don't use additional memory unlike merge sort algorithm

Cons :
 * Doesn't guarantee N * log N complexity, in worst case may give N^2
"""


def partition(array, start, end):
    # select pivot value
    pivot_value = array[start]

    left_marker = start
    right_marker = end

    while left_marker < right_marker:

        # find a number greater than pivot by using left marker
        while left_marker < right_marker and array[left_marker] <= pivot_value:
            left_marker += 1

        # find a number less than pivot value by using right marker
        while right_marker >= left_marker and array[right_marker] >= pivot_value:
            right_marker -= 1

        if left_marker < right_marker:
            array[left_marker], array[right_marker] = array[right_marker], array[left_marker]
        else:
            array[start], array[right_marker] = array[right_marker], array[start]

    return right_marker


def quickSortRecursiveHelper(array, start, end):
    if start < end:
        split_point = partition(array, start, end)

        quickSortRecursiveHelper(array, start, split_point - 1)
        quickSortRecursiveHelper(array, split_point + 1, end)


def quickSort(array):
    quickSortRecursiveHelper(array, 0, len(array) - 1)


def generateRandomArray(start, end, size):
    """Generate random array of numbers"""
    listArray = []

    for i in range(0, size):
        listArray.append(random.randint(start, end))

    return listArray


if __name__ == "__main__":
    randArray = generateRandomArray(0, 150, 7)
    for value in randArray:
        print(value, end=" ")

    print("\n Quick sort : ")
    quickSort(randArray)

    for value in randArray:
        print(value, end=" ")
