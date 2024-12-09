# A head-and-tail implementation of a deque


# Each node is an instance of class Node
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.nxt = next


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Add element n as last entry in deque
    def add_last(self, n):
        new = Node(n, None)
        if self.head is None:  # Empty queue
            self.head = new
            self.tail = new
        else:
            self.tail.nxt = new
            self.tail = new
        self.size += 1

    # Returns a string representation of the current deque content
    def __str__(self):
        s = "{ "
        node = self.head
        while node is not None:
            s += str(node.value) + " "
            node = node.nxt
        s += "}"
        return s

    # True if deque empty
    def is_empty(self):
        return self.size == 0

    # Add element n as first entry in deque
    def add_first(self, n):
        new = Node(n, self.head)
        if self.head is None:  # Empty queue
            self.tail = new
        self.head = new
        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Raises IndexError when accessing empty deque.
    def get_last(self):
        if self.tail is None:
            raise IndexError("You can't access an empty queue")
        return self.tail.value

    # Returns (without removing) the first entry in the deque
    # Raises IndexError when accessing empty deque.
    def get_first(self):
        if self.head is None:
            raise IndexError("You can't access an empty queue")
        return self.head.value

    # Removes and returns the first entry in the deque.
    # Raises IndexError when accessing empty deque.
    # The case size = 1 requires special handling
    def remove_first(self):
        if self.head is None:
            raise IndexError("You can't remove from an empty queue")

        value = self.head.value
        self.head = self.head.nxt # Initializing the new head

        if self.head is None:  # Queue is now empty
            self.tail = None
        self.size -= 1
        return value

    # Removes and returns the last entry in the deque.
    # Raises IndexError when accessing empty deque.
    # The case size = 1 requires special handling
    def remove_last(self):
        if self.tail is None:
            raise IndexError("You can't remove from an empty queue")

        if self.head == self.tail:  # Single element in queue
            value = self.tail.value
            self.head = None
            self.tail = None
        else:
            # Traverse to find the node before the last node
            node = self.head
            while node.nxt is not self.tail:
                node = node.nxt
            value = self.tail.value
            self.tail = node
            self.tail.nxt = None
        self.size -= 1
        return value

    # Returns an iterator over the deque
    # allowing for simple iteration over all elements
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.nxt
