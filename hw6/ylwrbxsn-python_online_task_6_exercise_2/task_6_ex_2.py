"""
Create CustomList – the linked list of values of random type, which size changes dynamically and has an ability to index
elements.

The task requires implementation of the following functionality:
• Create the empty user list and the one based on enumeration of values separated by commas. The elements are stored
in form of unidirectional linked list. Nodes of this list must be implemented in class Item.
    Method name: __init__(self, *data) -> None;
• Add and remove elements.
    Method names: append(self, value) -> None - to add to the end,
                add_start(self, value) -> None - to add to the start,
                remove(self, value) -> None - to remove the first occurrence of given value;
• Operations with elements by index. Negative indexing is not necessary.
    Method names: __getitem__(self, index) -> Any,
                __setitem__(self, index, data) -> None,
                __delitem__(self, index) -> None;
• Receive index of predetermined value.
    Method name: find(self, value) -> Any;
• Clear the list.
    Method name: clear(self) -> None;
• Receive lists length.
    Method name: __len__(self) -> int;
• Make CustomList iterable to use in for-loops;
    Method name: __iter__(self);
• Raise exceptions when:
    find() or remove() don't find specific value
    index out of bound at methods __getitem__, __setitem__, __delitem__.


Notes:
    The class CustomList must not inherit from anything (except from the object, of course).
    Function names should be as described above. Additional functionality has no naming requirements.
    Indexation starts with 0.
    List length changes while adding and removing elements.
    Inside the list the elements are connected as in a linked list, starting with link to head.
"""


class Item:
    """
    A node in a unidirectional linked list.
    """
    def __init__(self, item=None, next=None):
        self.elem = item
        self.next = next


class CustomList:
    """
    An unidirectional linked list.
    """

    def __init__(self, *data):
        self.__head = None

        if len(data) > 0:
            # self.__head = None
            for i in data:
                self.append(i)

    def append(self, value):
        node = Item(value, None)

        if self.__head is None:
            self.__head = node
            return

        itr = self.__head

        while x := itr.next:
            itr = x

        itr.next = node

    def add_start(self, data):
        node = Item(data, self.__head)
        self.__head = node

    def remove(self, value):
        try:
            if value == self.__head.elem:
                self.__head = self.__head.next
                return
            n = self.__head
            while n.next is not None:
                if value == n.next.elem:
                    break
                n = n.next
            n.next = n.next.next
        except Exception:
            raise ValueError

    def find(self, value):
        try:
            cur_node = self.__head
            cur_id = 0
            while True:
                if cur_node.elem == value:
                    return cur_id
                cur_id += 1
                cur_node = cur_node.next
        except Exception:
            raise ValueError

    def clear(self):
        self.__head = None

    def __getitem__(self, index):
        if index >= self.__len__():
            raise IndexError
        cur_id = 0
        cur_node = self.__head
        while True:
            if cur_id == index:
                return cur_node.elem
            cur_id += 1
            cur_node = cur_node.next

    def __setitem__(self, index, data):
        if index < 0 or index > self.__len__():
            raise IndexError

        if index == 0:
            self.add_start(data)
            return

        count = 0
        itr = self.__head
        while itr:
            if count == index - 1:
                node = Item(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def __delitem__(self, index):
        if index < 0 or index >= self.__len__():
            raise IndexError
        if index == 0:
            self.__head = self.__head.next
            return

        count = 0
        itr = self.__head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def __len__(self):
        itr = self.__head
        total = 0
        while itr:
            total += 1
            itr = itr.next
        return total

    def __iter__(self):
        current = self.__head
        while current is not None:
            yield current.elem
            current = current.next

    def print(self):
        itr = self.__head
        while itr:
            print(itr.elem)
            itr = itr.next


mylist = CustomList(1,2,3,4,5)
# mylist.print()
# mylist.append(15)
# mylist.add_start(10)
# mylist.remove(1)
# mylist.clear()
# mylist.print()

for i in mylist:
    print(i)