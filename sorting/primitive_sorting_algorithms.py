from utils import data_provider


def selection_sort(array):
    """
    O(N) : N^2
    Pos :
        * Low counts of write operations, each element writes from the first time
        exactly in a correct position

    Cons :
        * Make dummy operations if pass a sorted array on input
    """
    size = len(array)

    for i in range(0, size - 1):
        min_index = i

        # looking for the minimum value in unsorted part of array
        for j in range(i + 1, size):
            if array[min_index] > array[j]:
                min_index = j

        # swap minimum value in sorted part of array
        tmp = array[i]
        array[i] = array[min_index]
        array[min_index] = tmp

    return array


def insertion_sort(array):
    """
    O(N) : N^2

    Pos :
        * Linear complexity if pass a sorted array on input

    Cons :
        * More counts of write operations than in Selection sort algorithm
    """
    size = len(array)
    for i in range(1, size):
        index_to_insert = i

        while index_to_insert > 0 and array[index_to_insert - 1] > array[index_to_insert]:
            array[index_to_insert -
                  1], array[index_to_insert] = array[index_to_insert], array[index_to_insert - 1]
            index_to_insert -= 1

    return array


def bubble_sort(array):
    """
    O(N) : N^2

    Pos :
        * Linear complexity if pass a sorted array on input

    Cons :
        * More counts of write operations than in Selection sort algorithm
    """
    size = len(array)
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        index_sorted_part = 1

        for i in range(index_sorted_part, size):
            if array[i] < array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                is_sorted = False

        index_sorted_part += 1

    return array


if __name__ == "__main__":
    print("Selection sort : ")
    ordered_array = selection_sort(
        data_provider.generate_random_array(0, 150, 25))
    for value in ordered_array:
        print(value, end=" ")

    print("\nInsertion sort : ")
    ordered_array = insertion_sort(
        data_provider.generate_random_array(0, 150, 25))
    for value in ordered_array:
        print(value, end=" ")

    print("\nBubble sort : ")
    ordered_array = bubble_sort(
        data_provider.generate_random_array(0, 150, 25))
    for value in ordered_array:
        print(value, end=" ")
