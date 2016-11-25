class Tree:
    def __init__(self, root):
        self.root = Node(root)
    """
    When we are creating a new tree, we must always have a root element.
    For example:
    tree = Tree(root=5)
    """

    def add_child(self, parent, child):
        p_value = parent
        parent = self.__get(parent, self.root)
        print('Parent :' + str(parent.value))
        if parent:
            print('Added :' + str(child))
            return parent.children.append(Node(child, parent=parent))
        raise Exception('Parent {0} does not exists!'.format(p_value))

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

    def __get(self, to_find, root):
        if root == Node(to_find):
            return root
        if root.has_children():
            for child in root.children:
                print(child)
                return self.__get(to_find, child)
        return False

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
        return self.__height(self.root, 0)

    def __height(self, root, curr_height):
        print([x.value for x in root.children])
        if not root.children:
            return curr_height
        for child in root.children:
            return self.__height(child, curr_height + 1)

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
    def __init__(self, value, parent=None, children=[]):
        self.value = value
        self.children = children
        self.parent = parent

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
