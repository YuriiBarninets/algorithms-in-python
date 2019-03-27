import random


def selectionSort(array):
    """
    O(N) : N^2
    Pos :
        * Low counts of write operations, each element writes from the first time
        exactly in a correct position

    Cons :
        * Make dummy operations if pass a sorted array on input
    """
    N = len(array)

    for i in range(0, N - 1):
        min_index = i

        # looking for the minimum value in unsorted part of array
        for j in range(i + 1, N):
            if array[min_index] > array[j]:
                min_index = j

        # swap minimum value in sorted part of array
        tmp = array[i]
        array[i] = array[min_index]
        array[min_index] = tmp

    return array


def insertionSort(array):
    """
    O(N) : N^2

    Pos :
        * Linear complexity if pass a sorted array on input

    Cons :
        * More counts of write operations than in Selection sort algorithm
    """
    N = len(array)
    for i in range(1, N):
        indexToInsert = i

        while indexToInsert > 0 and array[indexToInsert - 1] > array[indexToInsert]:
            array[indexToInsert - 1], array[indexToInsert] = array[indexToInsert], array[indexToInsert - 1]
            indexToInsert -= 1

    return array


def bubbleSort(array):
    """
    O(N) : N^2

    Pos :
        * Linear complexity if pass a sorted array on input

    Cons :
        * More counts of write operations than in Selection sort algorithm
    """
    N = len(array)
    isSorted = False

    while not isSorted:
        isSorted = True
        indexSortedPart = 1

        for i in range(indexSortedPart, N):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                isSorted = False

        indexSortedPart += 1

    return array


def generateRandomArray(start, end, size):
    """Generate random array of numbers"""
    listArray = []
    
    for i in range(0, size):
        listArray.append(random.randint(start, end))
        
    return listArray


def sortingTest():
    print("Selection sort : ")
    ordered_array = selectionSort(generateRandomArray(0, 150, 25))
    for value in ordered_array:
        print(value, end=" ")

    print("\nInsertion sort : ")
    ordered_array = insertionSort(generateRandomArray(0, 150, 25))
    for value in ordered_array:
        print(value, end=" ")

    print("\nBubble sort : ")
    ordered_array = bubbleSort(generateRandomArray(0, 150, 25))
    for value in ordered_array:
        print(value, end=" ")


if __name__ == "__main__":
    sortingTest()
