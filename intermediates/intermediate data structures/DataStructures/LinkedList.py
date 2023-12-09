from abc import ABC, abstractmethod


class Node:

    """A Singular Node"""

    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class LinkedLists(ABC):
    @abstractmethod
    def __init__(self):
        self.head = None

    def __add__(self, other):
        """Returns a new concatenated linked list"""

        if not isinstance(other, (SinglyLinkedList, DoublyLinkedList)):
            raise TypeError("Unsupported operand type")

        if isinstance(self, SinglyLinkedList) and isinstance(other, SinglyLinkedList):
            result = SinglyLinkedList()
        elif isinstance(self, DoublyLinkedList) and isinstance(other, DoublyLinkedList):
            result = DoublyLinkedList()

        current = self.head
        while current:
            result.insert(current.data)
            current = current.next

        current = other.head
        while current:
            result.insert(current.data)
            current = current.next

        return result

    def __getitem__(self, idx):
        """Returns the node at the specified index"""

        # Slicing
        if isinstance(idx, slice):
            start, stop, step = idx.start, idx.stop, idx.step

            if start is None:
                start = 0
            if stop is None:
                stop = len(self)
            if step is None:
                step = 1

            if isinstance(self, SinglyLinkedList):
                sliced_list = SinglyLinkedList()
            elif isinstance(self, DoublyLinkedList):
                sliced_list = DoublyLinkedList()

            count = 0
            itr = self.head

            while itr and count < stop:
                if count >= start and count % step == 0:
                    sliced_list.insert(itr.data, -1)
                count += 1
                itr = itr.next

            return sliced_list

        # Negative indices
        if idx < 0:
            idx = len(self) + idx
            if idx < 0:
                raise IndexError("Index out of range")

        # Positive indices
        count = 0
        itr = self.head

        while count < idx:
            count += 1
            itr = itr.next

        return itr.data

    def __len__(self):
        """Returns the length of the linked list"""

        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def delete(self, idx=-1):
        """Deletes an node from a specific index. (default = end of linked list)"""

        # Deletes first node from the linked list
        if idx == 0:
            if self.head:
                self.head = self.head.next

        # Deletes last node from the linked list
        elif idx == -1:
            if self.head is None:
                return

            if self.head.next is None:
                self.head = None
                return

            itr = self.head
            while itr.next.next:
                itr = itr.next

            itr.next = None

        # Deletes node at the specified index from the linked list
        else:
            if idx < 0 or idx > len(self):
                raise IndexError("Index out of bounds")

            if idx == 0:
                self.head = self.head.next
                return

            count = 0
            itr = self.head
            while count < idx - 1:
                itr = itr.next
                count += 1

            itr.next = itr.next.next

    def insert(self, data, idx=0):
        """Insert nodes at a specified index (default = start of linked list)"""

        # Insert nodes one-by-one by iterating through the list
        if isinstance(data, list):
            for elem in data:
                if self.head is None:
                    self.head = Node(elem, None)
                    data.remove(elem)
                    self.insert(data)
                    return

                itr = self.head
                while itr.next:
                    itr = itr.next

                itr.next = Node(elem, None)

            return

        # Inserts a single node
        elif isinstance(data, (int, str, float)):
            # Inserts an node at the start
            if idx == 0:
                node = Node(data, self.head)
                self.head = node

            # Inserts an node at the end
            elif idx == -1:
                if self.head is None:
                    self.head = Node(data, None)
                    return

                itr = self.head
                while itr.next:
                    itr = itr.next

                itr.next = Node(data, None)
                return

            # Inserts an node at a specified index
            else:
                if idx < 0 or idx > len(self):
                    raise IndexError("Index out of bounds")

                if idx == 0:
                    node = Node(data, self.head)
                    self.head = node
                    return

                count = 0
                itr = self.head
                while count < idx - 1:
                    itr = itr.next
                    count += 1

                new_node = Node(data, itr.next)
                itr.next = new_node

        # Raises an error if argument is not of a specified type
        else:
            raise ValueError("Argument must be list, integer, string or float")

    def search(self, val):
        """Searches a specific value in the linked list and returns the first occurence"""

        idx = 0
        itr = self.head

        while itr:
            idx += 1
            itr = itr.next

            if itr.data == val:
                return idx

    def split(self, idx):
        """Splits the linked list into two linked lists at a specified"""

        if isinstance(self, SinglyLinkedList):
            left = SinglyLinkedList()
            right = SinglyLinkedList()
        elif isinstance(self, DoublyLinkedList):
            left = DoublyLinkedList()
            right = DoublyLinkedList()

        if idx < 0 or idx > len(self):
            raise IndexError("Index out of bounds")

        count = 0
        itr = self.head

        while count < idx:
            left.insert(itr.data)
            itr = itr.next
            count += 1

        while itr:
            right.insert(itr.data)
            itr = itr.next

        return left, right

    def update(self, val, idx):
        """Updates the value at a specified index"""

        count = 0
        itr = self.head

        while count < idx:
            count += 1
            itr = itr.next

        if itr is None:
            raise IndexError("Index out of bounds")

        itr.data = val


class CircularLinkedList(ABC):
    @abstractmethod
    def __init__(self):
        self.head = None

    def __getitem__(self, idx):
        """Returns the node at the specified index"""

        # Slicing
        if isinstance(idx, slice):
            start = idx.start % len(self) if idx.start is not None else 0
            stop = idx.stop % len(self) if idx.stop is not None else len(self)
            step = idx.step % len(self) if idx.step is not None else 1

            if isinstance(self, CircularSinglyLinkedList):
                sliced_list = CircularSinglyLinkedList()
            elif isinstance(self, CircularDoublyLinkedList):
                sliced_list = CircularDoublyLinkedList()

            count = 0
            itr = self.head

            while itr.next != self.head and count < stop:
                if count >= start and count % step == 0:
                    sliced_list.insert(itr.data)
                count += 1
                itr = itr.next

            return sliced_list

        # Negative indices
        if idx < 0:
            idx = (len(self) + idx) % len(self)
            if idx < 0:
                raise IndexError("Index out of range")

        # Positive indices
        count = 0
        itr = self.head

        while count < idx:
            count += 1
            itr = itr.next

        return itr.data

    def __len__(self):
        """Returns the length of the linked list"""

        count = 0
        itr = self.head
        while itr.next != self.head:
            count += 1
            itr = itr.next

        return count + 1

    def delete(self, idx):
        """Deletes a node at a specified index"""

        if idx < 0:
            raise IndexError("Index must be non-negative")

        if self.head is None:
            raise IndexError("Cannot delete from an empty linked list")

        itr = self.head
        count = 0

        while count < idx - 1:
            itr = itr.next
            count += 1

        if idx == 0:
            self.head = itr.next.next
        else:
            itr.next = itr.next.next

    def insert(self, data, idx=0):
        if isinstance(data, list):
            for elem in data:
                new_node = Node(elem, self.head)
                if self.head is None:
                    self.head = Node(elem, None)
                    self.head.next = self.head
                else:
                    itr = self.head
                    while itr.next != self.head:
                        itr = itr.next

                    itr.next = new_node

        elif isinstance(data, (int, str, float)):
            new_node = Node(data)

            if not self.head:
                self.head = new_node
                new_node.next = self.head
                return

            if idx == 0:
                new_node.next = self.head
                itr = self.head
                while itr.next != self.head:
                    itr = itr.next
                itr.next = new_node
                self.head = new_node

            elif idx == -1:
                if self.head is None:
                    self.head = new_node
                    new_node.next = self.head
                    return

                itr = self.head
                while itr.next != self.head:
                    itr = itr.next

                itr.next = new_node
                new_node.next = self.head

            else:
                count = 0
                itr = self.head

                while itr.next != self.head and count < idx - 1:
                    itr = itr.next
                    count += 1

                new_node.next = itr.next
                itr.next = new_node

    def search(self, val):
        """Searches a specific value in the linked list and returns the first occurence"""

        idx = 0
        itr = self.head

        while itr.next != self.head:
            idx += 1
            itr = itr.next

            if itr.data == val:
                return idx

    def update(self, val, idx):
        """Updates the value at a specified index"""

        idx = idx % len(self)
        count = 0
        itr = self.head

        while count < idx:
            count += 1
            itr = itr.next

        if itr is None:
            raise IndexError("Index out of bounds")

        itr.data = val


class SinglyLinkedList(LinkedLists):

    """Singly Linked List"""

    def __init__(self):
        self.head = None

    def __repr__(self):
        """Prints the singly linked list in a specific manner"""

        llstr = ""
        if self.head is None:
            llstr = "--> "

        else:
            itr = self.head
            while itr:
                llstr += str(itr.data) + " --> "
                itr = itr.next

        llstr = "(HEAD) " + llstr + "NULL"
        return llstr


class DoublyLinkedList(LinkedLists):

    """Doubly Linked List"""

    def __init__(self):
        self.head = None

    def __repr__(self):
        """Prints the doubly linked list in a specific manner"""

        dllstr = ""
        if self.head is None:
            dllstr = "<==> "

        else:
            itr = self.head
            while itr:
                dllstr += str(itr.data) + " <==> "
                itr = itr.next

        dllstr = "NULL <==> (HEAD) " + dllstr + "NULL"
        return dllstr

    def reverse(self):
        """Reverses a linked list"""

        result = DoublyLinkedList()
        nodes = []

        itr = self.head
        while itr:
            nodes.append(str(itr.data))
            itr = itr.next

        nodes = list(reversed(nodes))
        result.insert(nodes)

        return result


class CircularSinglyLinkedList(CircularLinkedList):

    """Circular Singly Linked List"""

    def __init__(self):
        self.head = None

    def __repr__(self):
        """Prints the linked list in a specific manner"""

        cllstr = ""
        if self.head is None:
            cllstr = "--> "

        else:
            itr = self.head

            while itr.next != self.head:
                cllstr += str(itr.data) + " --> "
                itr = itr.next

            if itr.next == self.head:
                cllstr += str(itr.data) + " --> "

        cllstr = "(HEAD) " + cllstr + "(HEAD)"
        return cllstr


class CircularDoublyLinkedList(CircularLinkedList):

    """Circular Doubly Linked List"""

    def __init__(self):
        self.head = None

    def __repr__(self):
        """Prints the doubly linked list in a specific manner"""

        cllstr = ""
        if self.head is None:
            cllstr = "<==> "

        else:
            itr = self.head

            while itr.next != self.head:
                cllstr += str(itr.data) + " <==> "
                itr = itr.next

            if itr.next == self.head:
                cllstr += str(itr.data) + " <==> "

        cllstr = "(HEAD) " + cllstr + "(HEAD)"
        return cllstr

    def reverse(self):
        """Reverses a linked list"""

        result = CircularDoublyLinkedList()
        nodes = []

        itr = self.head
        while itr.next != self.head:
            nodes.append(str(itr.data))
            itr = itr.next

        nodes.append(itr.data)

        nodes = list(reversed(nodes))
        result.insert(nodes)

        return result
