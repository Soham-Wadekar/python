class Node:

    """A Singular Node"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:

    """Singly Linked List"""

    def __init__(self):
        self.head = None

    def __add__(self, other):
        """Returns a new concatenated linked list"""

        if not isinstance(other, SinglyLinkedList):
            raise TypeError("Unsupported operand type")

        result = SinglyLinkedList()

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
        """Returns the element at the specified index"""

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

    def __repr__(self):
        """Prints the linked list in a specific manner"""

        llstr = ""
        if self.head is None:
            llstr = ""

        else:
            itr = self.head
            while itr:
                llstr += str(itr.data) + " ==> "
                itr = itr.next

        llstr = "(HEAD) " + llstr + "NULL"
        return llstr

    def delete(self, idx=-1):
        """Deletes an element from a specific index. (default = end of linked list)"""

        # Deletes first element from the linked list
        if idx == 0:
            if self.head:
                self.head = self.head.next

        # Deletes last element from the linked list
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

        # Deletes element at the specified index from the linked list
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
        """Insert elements at a specified index (default = start of linked list)"""

        # Insert elements one-by-one by iterating through the list
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

        # Inserts a single element
        elif isinstance(data, (int, str, float)):
            # Inserts an element at the start
            if idx == 0:
                node = Node(data, self.head)
                self.head = node

            # Inserts an element at the end
            elif idx == -1:
                if self.head is None:
                    self.head = Node(data, None)
                    return

                itr = self.head
                while itr.next:
                    itr = itr.next

                itr.next = Node(data, None)
                return

            # Inserts an element at a specified index
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

        left = SinglyLinkedList()
        right = SinglyLinkedList()

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
