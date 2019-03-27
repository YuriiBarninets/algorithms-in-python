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
        maxChild = self.left
        grandChild = maxChild.right

        if grandChild:
            while grandChild:
                maxChild = grandChild
                grandChild = maxChild.right

            self.value = maxChild.value
            maxChild.right = grandChild.left
        else:
            self.value = maxChild.value
            self.left = maxChild.left

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
        """Remove value from tree"""
        if self.root:
            self.root = self.removeFromNode(self.root, value)

    def removeFromNode(self, parent, value):
        """Implement recursive remove algorithm"""
        if parent is None:
            return None

        if parent.value == value:
            return parent.delete()
        elif parent.value > value:
            parent.left = self.removeFromNode(parent.left, value)
        else:
            parent.right = self.removeFromNode(parent.right, value)

        return parent


def performanceTest():
    """Check execution performance"""
    print("======== Performance test ========")
    n = 256
    while n <= 75000:
        binaryTree = BinaryTree()
        target = random.randint(0, n)

        for i in range(n):
            binaryTree.add(random.randint(0, n))

        begin = time()
        contains = binaryTree.contains(target)
        end = time()

        execution_time = (end - begin) * 10000
        print("N = {0}, target = {1}, contains = {2}, time = {3}".format(n, target, contains, execution_time))
        n *= 2


def removeAddContainsTest():
    print("======== Remove/Add/Contains test ========")
    binaryTree = BinaryTree()

    binaryTree.add(12)
    binaryTree.add(7)
    binaryTree.add(66)
    binaryTree.add(2)
    binaryTree.add(5)

    print(binaryTree.contains(7))

    binaryTree.remove(7)
    print(binaryTree.contains(7))


if __name__ == "__main__":
    performanceTest()
    removeAddContainsTest()


