from Heap import Heap
from Task import Task


print("Task Priority Queue Demo")

heap = Heap()

  # Create and add tasks
tasks = [
  Task(100, "Give mom a hug!"),
  Task(77, "walk outside"),
  Task(50, "Complete this assignment"),
  Task(90, "Call a friend"),
  Task(20, "Water the plants"),
  Task(15, "Drink water"),
  Task(15, "Go to gym"),
  Task(8, "Call grandma"),
  Task(73, "Plant the water"),
  Task(80, "Eat food"),
  ]

for task in tasks:
  heap.add(task)
  

print("Heap with tasks:")
for task in heap:
  print(task)
  
# Pull tasks based on priority
print("\nProcessing tasks:")
while not heap.is_empty():
  print(heap.pull_high())