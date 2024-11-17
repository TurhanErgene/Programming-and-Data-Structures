import os

def count_lines(path, depth=0):
  total_lines = 0
  indent = '    ' * depth

  if os.path.isdir(path):
    print(f"{indent}{path}/") 
    for entry in os.listdir(path):
      if not entry.startswith('.'):  # Ignore hidden files and directories.
        # print("path:", path)
        # print("entry:", entry)
        entry_path = os.path.join(path, entry) # https://www.geeksforgeeks.org/python-os-path-join-method/
        total_lines += count_lines(entry_path, depth + 1)
        
  elif path.endswith('.py') and os.path.isfile(path):
    print(f"{indent}{path}") 
    
    with open(path, 'r', encoding='utf-8') as file:
      lines = file.readlines()
      non_empty_lines = 0
      for line in lines:
        if line.strip():  # Check if the line is not empty or whitespace
          non_empty_lines += 1
      total_lines += non_empty_lines
  
  return total_lines


directory = input("Enter the directory path: ")
total = count_lines(directory)
print(f"\nTotal non-empty lines of Python code: {total}")