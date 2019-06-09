from utils import data_provider

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


def quick_sort_recursive_helper(array, start, end):
    if start < end:
        split_point = partition(array, start, end)

        quick_sort_recursive_helper(array, start, split_point - 1)
        quick_sort_recursive_helper(array, split_point + 1, end)


def quick_sort(array):
    quick_sort_recursive_helper(array, 0, len(array) - 1)


if __name__ == "__main__":
    rand_array = data_provider.generate_random_array(0, 150, 7)

    print("\nInput data : ")
    for value in rand_array:
        print(value, end=" ")

    print("\nQuick sort : ")
    quick_sort(rand_array)
    for value in rand_array:
        print(value, end=" ")
