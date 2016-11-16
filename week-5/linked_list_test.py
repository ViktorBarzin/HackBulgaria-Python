import unittest
from linked_list import LinkedList


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    def test_adding_element(self):
        self.ll.add_element(4)
        self.assertEqual(self.ll.size(), 1)

    def test_remove_element(self):
        self.ll.add_element(4)
        size = self.ll.size()
        self.ll.remove(0)
        size2 = self.ll.size()
        self.assertFalse(size == size2)

    def test_len_dunder(self):
        self.assertEqual(0, len(self.ll))

    def test_size(self):
        self.ll = LinkedList(10)
        self.assertEqual(self.ll.size(), 10)

    def test_size_after_adding(self):
        self.ll.add_element(10)
        self.assertEqual(1,self.ll.size())

    def test_size_after_remove(self):
        self.ll.add_element(10)
        self.ll.remove(0)
        self.assertEqual(0, self.ll.size())

    def test_pprint(self):
        self.ll.add_element(10)
        self.ll.add_element(100)
        self.ll.add_element(1000)
        self.assertEqual('[10, 100, 1000]', self.ll.pprint())

    def test_to_list(self):
        self.ll.add_element(100)
        self.ll.add_element(1000)
        self.ll.add_element(100)
        self.ll.add_element(1000)
        self.assertEqual([100, 1000, 100, 1000], self.ll.to_list())

    def test_index(self):
        self.ll.add_element(100)
        self.ll.add_element(1000)
        self.assertEqual(1000, self.ll.index(1).value)

    def test_add_at_index(self):
        self.ll.add_element(100)
        self.ll.add_element(1000)
        self.ll.add_at_index(1, 69)
        self.assertEqual(69, self.ll.index(1).value)

    def test_add_first(self):
        self.ll.add_element(100)
        self.ll.add_first(69)
        self.assertEqual(69, self.ll.index(0).value)

    def test_add_list(self):
        self.ll.add_element(1)
        self.ll.add_list([10, 100, 1000])
        self.assertEqual([1, 10, 100, 1000], self.ll.to_list())

    def test_add_linked_list(self):
        self.ll.add_element(1)
        new_ll = LinkedList()
        new_ll.add_element(10)
        new_ll.add_element(100)
        self.ll.add_linked_list(new_ll)
        self.assertEqual([1, 10, 100], self.ll.to_list())

    # def test_ll_from_to(self):
    #     self.ll.add_element(0)
    #     self.ll.add_list([1, 10, 100, 1000])
    #     self.assertEqual([10, 100], self.ll.ll_from_to(1, 2).to_list())

    def test_pop(self):
        self.ll.add_element(1)
        self.ll.add_element(10)
        self.ll.pop()
        self.assertEqual([1], self.ll.to_list())

    def reduce_to_unique(self):
        self.ll.add_element(1)
        self.ll.add_list([10, 100, 10])
        self.assertEqual([1, 10, 100], self.ll.reduce_to_unique())

    def test_set_element(self):
        self.ll.add_element(1)
        self.ll.add_list([10, 100, 1000])
        self.ll.set_element(2, 69)
        self.assertEqual(69, self.ll.index(2).value)

if __name__ == '__main__':
    unittest.main()