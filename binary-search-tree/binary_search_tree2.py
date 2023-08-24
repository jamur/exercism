class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        fmt = 'TreeNode(data={}, left={}, right={})'
        return fmt.format(self.data, self.left, self.right)

    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)

    def __iter__(self):
        if self.left is not None:
            yield from self.left
        yield self.data
        if self.right is not None:
            yield from self.right

class BinarySearchTree(object):
    def __init__(self, tree_data):
        root, *rest = tree_data
        self._data = TreeNode(root)
        for data in rest:
            self._data.insert(data)
    def data(self):
        return self._data
    def sorted_data(self):
        return list(self._data)
    def __iter__(self):
        yield from self._data

if __name__ == "__main__":
    tree = BinarySearchTree([5,1,2,3,8,1,1,4])
    print(tree.data())
    print(tree.sorted_data())
    for n in tree:
        print(n)
