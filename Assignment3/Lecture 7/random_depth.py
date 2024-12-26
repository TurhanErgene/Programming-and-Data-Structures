import random
import math
import matplotlib.pyplot as plt
from BstSet import BstSet

def generate_random_bst(size):
    """
    Generate a BST with `size` unique random elements.
    Returns the BST and the max depth of the tree.
    """
    bst = BstSet()
    elements = random.sample(range(1, size * 10), size)  # Generate `size` unique random numbers
    for elem in elements:
        bst.add(elem)
    return bst.max_depth()

def compute_mean_max_depth(sizes, runs=10):
    """
    Compute the mean max depth of random BSTs for given sizes over a specified number of runs.
    """
    mean_depths = []
    for size in sizes:
        depths = [generate_random_bst(size) for _ in range(runs)]
        mean_depth = sum(depths) / len(depths)
        mean_depths.append(mean_depth)
    return mean_depths

def complete_tree_depth(sizes):
    """
    Compute the depth of a complete binary tree for given sizes.
    """
    return [math.ceil(math.log2(size + 1)) for size in sizes]

def main():
    # Sizes for the trees: 2**h - 1 for h = 5, 6, ..., 19, 20
    sizes = [2**h - 1 for h in range(5, 21)]
    
    # Compute mean max depth for random BSTs
    mean_max_depths = compute_mean_max_depth(sizes)

    # Compute depth for complete binary trees
    complete_depths = complete_tree_depth(sizes)

    # Plot: Tree sizes vs Average Max Depth
    plt.figure()
    plt.plot(sizes, mean_max_depths, label="Random BST (Average Max Depth)", marker="o")
    plt.plot(sizes, complete_depths, label="Complete Tree Depth", marker="x")
    plt.xlabel("Tree Size")
    plt.ylabel("Depth")
    plt.title("Tree Size vs Depth")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot: log2(Tree sizes) vs Average Max Depth
    log_sizes = [math.log2(size) for size in sizes]
    plt.figure()
    plt.plot(log_sizes, mean_max_depths, label="Random BST (Average Max Depth)", marker="o")
    plt.xlabel("log2(Tree Size)")
    plt.ylabel("Depth")
    plt.title("log2(Tree Size) vs Depth")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
