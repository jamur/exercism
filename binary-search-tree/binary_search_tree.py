class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'

class BinarySearchTree:
    def __init__(self, tree_data):
        root, *tree_data = tree_data
        self._root = TreeNode(root)
        for data in tree_data:
            self._insert(data, self._root)

    def _insert(self, data, curr_node):
        if data <= curr_node.data:
            if not curr_node.left:
                curr_node.left = TreeNode(data)
            else:
                self._insert(data, curr_node.left)
        else:
            if not curr_node.right:
                curr_node.right = TreeNode(data)
            else:
                self._insert(data, curr_node.right)

    def data(self):
        return self._root

    def sorted_data(self):
        return list(self)

    def _generate_sorted_tree_data(self, curr_node):
        if not curr_node: # leaf node just reached (this child node is None)
            return
        yield from self._generate_sorted_tree_data(curr_node.left)
        yield curr_node.data
        yield from self._generate_sorted_tree_data(curr_node.right)

    def __iter__(self):
        yield from self._generate_sorted_tree_data(self._root)


if __name__ == "__main__":
    tree = BinarySearchTree([5,1,2,3,8,1,1,4])
    print(tree.data())
    print(tree.sorted_data())
    for n in tree:
        print(n)
