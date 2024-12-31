import random
from BstSet import BstSet 

def generate_random_tree(size):
    """Generate a BST with `size` unique random elements."""
    bst = BstSet()           
    elements = random.sample(range(1, size * 10), size)  # Generate unique random numbers from 1 to 10230 with 1023 elements 
    for elem in elements:
        bst.add(elem)
    return bst, elements


def save_dot_file(bst, filename):
    """Save the DOT representation of the tree to a file."""
    with open(filename, 'w') as file:
        file.write(bst.dot())


def perform_deletions_and_additions(bst, elements, iterations=2000, delete_count=512):
    """Perform repeated deletions and additions on the tree."""
    for _ in range(iterations):
        # Randomly select `delete_count` elements to delete
        to_delete = random.sample(elements, delete_count)
        
        # Delete the selected elements
        for elem in to_delete:
            bst.delete(elem)
        
        # Add the same elements back
        for elem in to_delete:
            bst.add(elem)


def main():
    # (a) Generate a random tree with 1023 unique values
    size = 1023
    bst, elements = generate_random_tree(size)
    
    # (b) Save the initial tree (DOT format) to before_delete.txt
    save_dot_file(bst, './Lecture 7/before_delete.txt')
    
    # (c) Perform deletions and additions 2000 times
    perform_deletions_and_additions(bst, elements, iterations=2000, delete_count=512)
    
    # (d) Save the final tree (DOT format) to after_delete.txt
    save_dot_file(bst, './Lecture 7/after_delete.txt')


main()
