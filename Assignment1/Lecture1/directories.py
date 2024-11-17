import os

def print_files(dir_path):
  for entry in os.listdir(dir_path):
    full_path = os.path.join(dir_path, entry)
    if os.path.isdir(full_path):
      print_files(full_path)
    else:
      print(full_path)

directory_path = './'
print_files(directory_path)


#https://www.geeksforgeeks.org/python-list-all-files-in-directory-and-subdirectories/