from time import time
import random

'''
Binary search algorithm in array

Pros :
 * O(N) = log(n) 

Cons :
 * Data in an array must be sorted
 * Algorithm requires continuous array of sorted data
 * It's difficult to support efficient update/insert/remove operation under such array,
   because it requires to recreate/move all data when we update/insert/remove a new element into an array
'''


def binary_search(ordered_collection, target):
    low = 0
    high = len(ordered_collection) - 1

    while low <= high:
        mid = (low + high) // 2

        if target == ordered_collection[mid]:
            return mid
        elif target < ordered_collection[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def performance_test():
    n = 256
    print("======== Binary search algorithm ========")

    while n < 10000000:
        sorted_list = list(range(n))
        target = random.randint(0, n)

        begin = time()
        position = binary_search(sorted_list, target)
        end = time()

        execution_time = (end - begin) * 10000
        print("N = {0}, target = {1}, pos = {2}, time = {3}".format(n, target, position, execution_time))
        n *= 2


if __name__ == "__main__":
    performance_test()
