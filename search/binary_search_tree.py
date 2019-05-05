import random
from time import time

'''
Binary search tree data structure
BST Properties :
 * All values on the left side of a node is smaller or equal the root's value
 * All values on the right side of a node is bigger than the root's value
 
Pos :
 * Doesn't require continuous array of sorted data
 * Value could be easily add/delete without necessarily to reallocate data as we must do with binary search array
 
Cons :
 * Data is more segmented
 * Require balancing algorithm in order to avoid degeneration into a linear list 

'''


class BinaryNode:
    def __init__(self, value = None):
        """Create empty Binary node"""
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        """Add a new node to the tree containg this value"""
        if self.value >= value:
            if self.left:
                self.left.add(value)
            else:
                self.left = BinaryNode(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = BinaryNode(value)

    def delete(self):
        # first case : if there no child then just delete node
        if (self.left is None) and (self.right is None):
            return None

        # second case : if there is only one child then this child becomes on place of deleted node
        if self.left is None:
            return self.right

        if self.right is None:
            return self.left

        # third case : if there are 2 children then find the maximum child on the left side
        max_child = self.left
        grand_child = max_child.right

        if grand_child:
            while grand_child:
                parent = max_child
                max_child = grand_child
                grand_child = max_child.right

            self.value = max_child.value
            parent.right = max_child.left
        else:
            self.value = max_child.value
            self.left = max_child.left

        return None


class BinaryTree:
    def __init__(self):
        """Create empty Binary Tree"""
        self.root = None

    def add(self, value):
        """Insert value into proper location in Binary Tree"""
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)

    def contains(self, value):
        """Check whether value exist in BST"""
        node = self.root

        while node:
            if node.value == value:
                return True
            elif node.value >= value:
                node = node.left
            else:
                node = node.right

        return False

    def remove(self, value):
        """Run recursive algorithm from ROOT node when removes value from the tree"""
        if self.root:
            self.root = self.remove_from_node(self.root, value)

    def remove_from_node(self, parent, value):
        """Implement recursive remove algorithm"""
        if parent is None:
            return None

        if parent.value == value:
            return parent.delete()
        elif parent.value > value:
            parent.left = self.remove_from_node(parent.left, value)
        else:
            parent.right = self.remove_from_node(parent.right, value)

        return parent


def performance_test():
    """Check execution performance"""
    print("======== Performance test ========")
    n = 256
    while n <= 75000:
        binary_tree = BinaryTree()
        target = random.randint(0, n)

        for i in range(n):
            binary_tree.add(random.randint(0, n))

        begin = time()
        contains = binary_tree.contains(target)
        end = time()

        execution_time = (end - begin) * 10000
        print("N = {0}, target = {1}, contains = {2}, time = {3}".format(n, target, contains, execution_time))
        n *= 2


def remove_add_contains_test():
    print("======== Remove/Add/Contains test ========")
    binary_tree = BinaryTree()

    binary_tree.add(12)
    binary_tree.add(7)
    binary_tree.add(66)
    binary_tree.add(2)
    binary_tree.add(5)

    print(binary_tree.contains(7))
    binary_tree.remove(7)
    print(binary_tree.contains(7))


if __name__ == "__main__":
    performance_test()
    remove_add_contains_test()


