class LinkedList:
    def __init__(self, initial_size=0):
        self.__size = initial_size
        self.head = None
        self.tail = None

    def __len__(self):
        return self.__size

    def add_element(self, data):
        if self.size() == 0:
            self.head = Node(data)
            self.__size += 1
            self.tail = self.head
            return self.head

        new_node = Node(data)
        self.tail.next_item = new_node
        self.tail = new_node
        self.__size += 1
        return data

    def index(self, index):
        result_item = self.head
        for i in range(index):
            # print(result_item)
            result_item = result_item.next_item
        return result_item

    def size(self):
        return self.__size

    def remove(self, index):
        previous_item = self.index(index - 1)
        previous_item.next_item = self.index(index + 1)
        self.__size -= 1

    def pprint(self):
        result = '['
        next_item = self.head
        while next_item is not None:
            if next_item.next_item is not None:
                result += '{0}, '.format(str(next_item))
                next_item = next_item.next_item
            else:
                return result + str(next_item) + ']'

        return result + ']'

    def to_list(self):
        result_list = []
        item = self.head
        while item is not None:
            result_list.append(item.value)
            item = item.next_item
        return result_list

    def add_at_index(self, index, data):
        previous_item = self.index(index - 1)
        # Save the previous item's next item
        old_item_next = previous_item.next_item
        new_item = Node(data)
        # Add previous item's next item to the new item
        previous_item.next_item = new_item
        # Set new item's next item
        new_item.next_item = old_item_next
        self.__size += 1

    def add_first(self, data):
        prev_head = self.head
        self.head = Node(data)
        self.head.next_item = prev_head
        self.__size += 1

    def add_list(self, new_list: list):
        for i in new_list:
            # Get last item
            last_item = self.tail
            new_node = Node(i)
            # Update last item's next item
            last_item.next_item = new_node
            # Update tail
            self.tail = new_node
        self.__size += len(new_list)

    def add_linked_list(self, linked_list):
        a = linked_list.to_list()
        self.add_list(a)
        self.__size += len(linked_list)

    def ll_from_to(self, start_index, end_index):
        new_ll = LinkedList()
        head = self.index(start_index)
        for i in range(end_index - start_index + 1):
            new_ll.add_element(head.value)
            head = head.next_item
        print(type(new_ll))
        return new_ll

    def pop(self):
        current = self.head
        c_next = current.next_item
        counter = 0
        while c_next is not None:
            current = c_next
            c_next = c_next.next_item
            counter += 1
        self.remove(counter)
        return current.next_item

    def reduce_to_unique(self):
        seen_items = []
        current = self.head
        while current.next_item is not None:
            if current.next_item.value not in seen_items:
                seen_items.append(current.next_item.value)
        self = LinkedList()
        self.add_list([seen_items])
        return self

    def set_element(self, index, data):
        to_change = self.index(index)
        to_change.value = data
        return to_change.value


class Node:
    def __init__(self, value, next_item=None, prev=None):
        self.value = value
        self.next_item = next_item
        self.prev = prev

    def __str__(self):
        return str(self.value)