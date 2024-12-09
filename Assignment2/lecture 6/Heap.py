class Heap:
    def __init__(self):
        self.heap = []


    # String representation of the heap
    def __str__(self):
        return str(self.heap)
    

    # Get current heap size
    def get_size(self):
        return len(self.heap)
    

    # Check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0
    

    # Peek at the highest priority element
    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0]
    

    # Add element to the heap
    def add(self, elem):
        self.heap.append(elem)
        self._heapify_up(len(self.heap) - 1)  


     # Pull highest from heap
    def pull_high(self):
        if self.is_empty():
            raise IndexError("Cannot pull_high from an empty array")   
       
        highest = self.heap[0]

        if len(self.heap) == 1:
            return self.heap.pop()
        
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return highest

    
    # [1, 4, 6, 8, 3, 1]
    def _heapify_up(self, index): 
        parent = (index - 1) // 2

        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index] # atomic operation!
            index = parent
            parent= (index - 1) // 2


    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap [largest]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest


    # Support for iteration over all elements
    def __iter__(self):
        return iter(self.heap)
