class Task:
  def __init__(self, priority, description):
    self.priority = priority
    self.description = description


  def __repr__(self):
    return f"[{self.priority}, {self.description}]"


  # Comparison operators for heap
  def __lt__(self, other):
    return self.priority < other.priority
  
  def __le__(self, other):
    return self.priority <= other.priority
  
  def __gt__(self, other):
    return self.priority > other.priority
  
  def __ge__(self, other):
    return self.priority >= other.priority

