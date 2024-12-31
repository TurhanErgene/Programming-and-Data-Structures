from AvlSet import AvlSet
import random
import math
import matplotlib.pyplot as plt


class BstNode:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def add(self, val):
        if val < self.value:
            if self.left is None:
                self.left = BstNode(val, None, None)
            else:
                self.left.add(val)
        elif val > self.value:
            if self.right is None:
                self.right = BstNode(val, None, None)
            else:
                self.right.add(val)

  
    def max_depth(self):
        if self is None:
            return 0

        left_depth = self.left.max_depth() if self.left else 0
        right_depth = self.right.max_depth() if self.right else 0

        return 1 + max(left_depth, right_depth)

class BstSet:

    def __init__(self):
        self.root = None

    # Adds value val to tree (if it doesn't already exist)
    def add(self, val):
        if self.root is None:
            self.root = BstNode(val, None, None)
        else:
            self.root.add(val)

    
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()


def generate_random_avl(size):
    avl = AvlSet()
    elements = random.sample(range(1, size * 10), size)  # Random elements from 1 to size * 10 (inclusive) without replacement
    for elem in elements:
        avl.add(elem)
    return avl.max_depth()

def generate_random_bst(size):
    """
    Generate a BST with `size` unique random elements.
    Returns the BST and the max depth of the tree.
    """
    bst = BstSet()
    elements = random.sample(range(1, size * 10), size)  # Random elements from 1 to size * 10 (inclusive) without replacement 
    for elem in elements:
        bst.add(elem)
    return bst.max_depth()


def compute_mean_max_depth(sizes, runs=8):
    bst_depths = []
    avl_depths = []

    for size in sizes:
        bst_avg = 0
        avl_avg = 0

        for _ in range(runs):
            bst_avg += generate_random_bst(size)
            avl_avg += generate_random_avl(size)

        bst_depths.append(bst_avg / runs)
        avl_depths.append(avl_avg / runs)

    return bst_depths, avl_depths

# def complete_tree_depth(sizes):
#     """
#     Compute the depth of a complete binary tree for given sizes.
#     """
#     return [math.ceil(math.log2(size + 1)) for size in sizes]

def plot_results(sizes, bst_depths, avl_depths):
    """
    Plot tree size vs average max depth for AVL and BST.
    """
    complete_depths = [math.ceil(math.log2(size + 1)) for size in sizes]

    # Plot: Tree sizes vs Average Max Depth
    plt.figure(figsize=(12, 6))

    # Linear scale
    plt.subplot(1, 2, 1)
    plt.plot(sizes, complete_depths, 'b+', label="Complete Tree Depth")
    plt.plot(sizes, bst_depths, 'g^', label="BST Average Depth")
    plt.plot(sizes, avl_depths, 'r*', label="AVL Average Depth")
    plt.xlabel("Tree Size")
    plt.ylabel("Max Depth (average of 8 runs)")
    plt.title("Depth of Random Input Trees")
    plt.legend()
    plt.grid(True)

    # Log scale
    plt.subplot(1, 2, 2)
    log_sizes = [math.log2(size) for size in sizes]
    plt.plot(log_sizes, complete_depths, 'b+', label="Complete Tree Depth")
    plt.plot(log_sizes, bst_depths, 'g^', label="BST Average Depth")
    plt.plot(log_sizes, avl_depths, 'r*', label="AVL Average Depth")
    plt.xlabel("log2(Tree Size)")
    plt.ylabel("Max Depth (average of 8 runs)")
    plt.title("Log(Tree Size) vs Depth")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Main function to tie everything together
def main():
    # Sizes for the trees: 2^h - 1 for h = 3, 4, ..., 17, 18
    sizes = [2**h - 1 for h in range(3, 18)]

    # Compute mean max depth for random BSTs and AVL trees
    bst_depths, avl_depths = compute_mean_max_depth(sizes)

    # Plot the results
    plot_results(sizes, bst_depths, avl_depths)


main()