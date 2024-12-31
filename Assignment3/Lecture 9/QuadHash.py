import math


class QuadHash:
    def __init__(self, capacity = 11):
        self._size = capacity
        self._count = 0
        self._table = [None] * capacity

    def hash_function(self, key):
        hash_value = key.__hash__()

        if hash_value <= 0:
            hash_value = -hash_value

        return hash_value % self._size

    # It is always a good idea to increase the size of the table with a prime number
    # This is especially true for open addressing algorithms
    # This function calculates the next available prime when doubling
    # The return value should be that number
    def _next_prime(self, n):
        def is_prime(num):
            if num < 2: return False
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        while not is_prime(n):
            n += 1
        return n

    def _rehash(self):
        old_table = self._table
        self._size = self._next_prime(2 * self._size)
        self._table = [None] * self._size
        self._count = 0
        for item in old_table:
            if item:
                self.add(item)

    def add(self, key):
        if self._count / self._size > 0.7:
            self._rehash()

        index = self.hash_function(key)
        i = 1
        while self._table[index] is not None:
            if self._table[index] == key:  # Prevent duplicate insertion
                return
            index = (index + i**2) % self._size
            i += 1

        self._table[index] = key  # Store the object itself, not None
        self._count += 1

    def contains(self, key):
        index = self.hash_function(key)
        i = 1
        while self._table[index] is not None:
            if self._table[index] == key:
                return True
            index = (index + i**2) % self._size
            i += 1
        return False

    # To solve the task of counting words and using a hash table, you will need to implement one additional method—get(). It should not be that much of a problem as it is basically the same as contains(), but it needs to return an object (and this is important, not a string or string representation of the object, but the object itself). So please add this method even though it is not part of the skeleton.
    def get(self, key):
        index = self.hash_function(key)
        i = 1
        while self._table[index] is not None:
            if self._table[index] == key:
                return self._table[index]  # Return the stored object
            index = (index + i**2) % self._size
            i += 1
        return None  # Explicitly return None if not found
    
    def __str__(self):
        result = ''
        for i in range(self._size):
            result += f'[{i}]: '
            result += str(self._table[i])

            result += '\n'

        return result

    def __iter__(self):
        return QuadHashIterator(self)

class QuadHashIterator:
    def __init__(self, hash_table):
        self._table = hash_table._table
        self._current = 0
        self._size = hash_table._size

    def __next__(self):
        while self._current < self._size:
            item = self._table[self._current]
            self._current += 1
            if item is not None:
                return item
        raise StopIteration

