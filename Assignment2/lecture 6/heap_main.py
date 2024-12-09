from Heap import Heap
import random

print("Heap Demo")
heap = Heap()

# Add some elements
# for i in range(8):
#     rand_int = random.randint(1,20)
#     heap.add(rand_int)
# to avoid repetitive elements
heap.add(10)
heap.add(1)
heap.add(24)
heap.add(2)
heap.add(8)
heap.add(3)
heap.add(11)

print("Heap after additions:", heap)

# Peek and pull highest priority elements
print("Peek:", heap.peek())
print("Pull:", heap.pull_high())
print("Heap after pull:", heap)

# Iterate through heap
for elem in heap:
    print(elem, end=" ")
print()