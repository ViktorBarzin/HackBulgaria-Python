class Tree:
    def __init__(self, root):
        self.root = Node(root, depth=0)
    """
    When we are creating a new tree, we must always have a root element.
    For example:
    tree = Tree(root=5)
    """

    def add_child(self, parent, child):
        parent = Node(parent, depth=parent.depth)
        if parent.value == self.root.value:
            new_node = Node(child, parent=parent, depth=1)
            self.root.children.append(new_node)
        else:
            print('Creating {0} with parent {1}'.format(child, parent.depth))
            new_node = Node(child, parent=parent, depth=parent.depth + 1)
            parent.children.append(new_node)

    """
    When we are adding new element to our tree, we must specify the parent:
    tree = Tree(root=5)
    tree.add(parent=5, child=4)
    tree.add(parent=5, child=3)
    tree.add(parent=4, child=2)

    This will make the following tree:

        5
       / \
      4   3
     /
    2
    """

    def find(self, x):
        visited, queue = set(), [self.root]
        while queue:
            current = queue.pop()
            if current == Node(x):
                return current.value
            if current.has_children() and current not in visited:
                queue.extend(current.children)
                for child in current.children:
                    visited.add(child)
        return False
    """
        Returns True or False if Node with value x is present in the tree
    """

    def height(self):
        max_height = 0
        visited, queue = set(), [self.root]
        while queue:
            current = queue.pop()
            print(current.value, current.depth)
            if current.depth > max_height:
                max_height = current.depth
            if current.has_children() and current not in visited:
                queue.extend(current.children)
                for child in current.children:
                    visited.add(child)
        return max_height

    """
        Returns an integer number of the max height of the tree
          5
         / \
        4   3
       /
      2

      tree.height() = 2
    """

    def count_nodes(self):
        pass
    """
        Returns the number of node sin the tree
        In our example -> tree.count_nodes() = 4
    """

    def tree_levels(self):
        pass
    """
        Returns a list of lists with the nodes foe each level1
        tree.tree_levels = [[5], [4, 3], [2]]
    """


class Node:
    def __init__(self, value, depth,parent=None, children=[],):
        self.value = value
        self.children = children
        self.parent = parent
        self.depth = depth

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return self.value

    def has_children(self):
        return len(self.children) > 0


def main():
    pass

if __name__ == '__main__':
    main()
