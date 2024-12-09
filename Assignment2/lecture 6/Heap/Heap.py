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
    
    
  # Support for iteration over all elements
  def __iter__(self):
    pass
