from utils import data_provider

'''
Binary heap data structure
Can be used for sorting(HeapSort) - insert all items and then extract them.
Can be used to implement priority queue.

Binary heap properties :
 * All level except the last one must be filled (complete property)
 * A child is always greater/smaller than its parent (heap-order property)
 
An implementation of a binary heap using an array.
The root of the heap can be found in the first element of the array.
For given an index i, it is possible to find the indices of the parent/child elements in the tree.
'''


class BinaryHeap:
    def __init__(self, comparator=None):
        self._items = []
        self._comparator = comparator if comparator is not None else lambda a, b: a < b

    def add(self, item):
        self._items.append(item)
        self.bubble_up(self.size() - 1)

    def extract_top(self):
        self.swap(0, self.size() - 1)
        result = self._items.pop()
        self.bubble_down(0)

        return result

    def peek(self):
        return self._items[0]

    def size(self):
        return len(self._items)

    def parent_index(self, index):
        return (index - 1) // 2

    def left_child_index(self, index):
        return index * 2 + 1

    def right_child_index(self, index):
        return index * 2 + 2

    def has_children(self, index):
        return self.item_exists(self.left_child_index(index))

    def item_exists(self, index):
        return 0 <= index < self.size()

    def swap(self, index1, index2):
        self._items[index1], self._items[index2] = self._items[index2], self._items[index1]

    def bubble_up(self, index):
        while True:
            parent_index = self.parent_index(index)

            if self.item_exists(parent_index) is False:
                break

            result = self._comparator(
                self._items[index], self._items[parent_index])
            if result is True:
                self.swap(index, parent_index)
                index = parent_index
            else:
                break

    def bubble_down(self, index):
        while True:
            if self.has_children(index) is False:
                break

            child_index_to_swap = self.find_child_index_for_bubble_down(index)
            result = self._comparator(
                self._items[index], self._items[child_index_to_swap])
            if result is False:
                self.swap(index, child_index_to_swap)
                index = child_index_to_swap
            else:
                break

    def find_child_index_for_bubble_down(self, index):
        left_child_index = self.left_child_index(index)
        right_child_index = self.right_child_index(index)

        # if there are 2 children find smaller/bigger of them
        if self.item_exists(left_child_index) and self.item_exists(right_child_index):
            return left_child_index if self._comparator(self._items[left_child_index], self._items[right_child_index])\
                else right_child_index

        # if there is only single child
        return left_child_index


def heap_sort(array):
    heap = BinaryHeap()

    # pushing an item one by one into the heap,
    # then retrieving them in the sorted order
    for item in array:
        heap.add(item)

    array.clear()
    while heap.size() > 0:
        array.append(heap.extract_top())


if __name__ == "__main__":
    rand_array = data_provider.generate_random_array(0, 150, 15)
    for value in rand_array:
        print(value, end=" ")

    print("\n Heap sort : ")
    heap_sort(rand_array)

    for value in rand_array:
        print(value, end=" ")
