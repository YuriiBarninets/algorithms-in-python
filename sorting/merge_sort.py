import sys
sys.path.append("../utils")
import data_provider


"""
O(N) : N * log N
Worst case : N * log N

Pos :
 * Guarantee N * log N complexity unlike QuickSort

Cons :
 * Use additional memory for merge two sub arrays
"""


# Merges two subarrays of arr[]
# First subarray arr[left..middle]
# Second subarray arr[middle+1..right]
def merge(arr, left, middle, right):
    num1 = middle - left + 1
    num2 = right - middle

    left_arr = [0] * num1
    right_arr = [0] * num2

    # copy data to first subarray
    for i in range(0, num1):
        left_arr[i] = arr[left + i]

    # copy data to second subarray
    for j in range(0, num2):
        right_arr[j] = arr[middle + 1 + j]

    # merge the temp arrays back into arr[left..right]
    i = 0 # index of first subarray
    j = 0 # index of second subarray
    k = left # index of merged subarray

    # merge operation
    while i < num1 and j < num2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    # copy the remaining elements of left_arr[], if there are any
    while i < num1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    # copy the remaining elements of right_arr[], if there are any
    while j < num2:
        arr[k] = right_arr[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        middle = (left + right) // 2

        # sort first and second halves
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)
        merge(arr, left, middle, right)


if __name__ == "__main__":
    rand_array = data_provider.generate_random_array(0, 150, 15)
    for value in rand_array:
        print(value, end=" ")

    print("\nMerge sort : ")
    merge_sort(rand_array, 0, len(rand_array) - 1)

    for value in rand_array:
        print(value, end=" ")
