import random

def generate_random_integers(size, min_value, max_value):
    """
    Generate a list of random integers.
    
    :param size: Number of elements in the list.
    :param min_value: Minimum value of the integers.
    :param max_value: Maximum value of the integers.
    :return: List of random integers.
    """
    return [random.randint(min_value, max_value) for _ in range(size)]


def generate_sorted_list(size, min_value, max_value, order="ascending"):
    """
    Generate a sorted list of integers.
    
    :param size: Number of elements in the list.
    :param min_value: Minimum value of the integers.
    :param max_value: Maximum value of the integers.
    :param order: "ascending" or "descending".
    :return: Sorted list of integers.
    """
    lst = [random.randint(min_value, max_value) for _ in range(size)]
    return sorted(lst) if order == "ascending" else sorted(lst, reverse=True)


def generate_repeated_values(size, value):
    """
    Generate a list with all elements being the same value.
    
    :param size: Number of elements in the list.
    :param value: The repeated value.
    :return: List with repeated values.
    """
    return [value for _ in range(size)]


def generate_floats(size, min_value, max_value, decimals=2):
    """
    Generate a list of random floating-point numbers.
    
    :param size: Number of elements in the list.
    :param min_value: Minimum value of the floats.
    :param max_value: Maximum value of the floats.
    :param decimals: Number of decimal places.
    :return: List of random floats.
    """
    return [round(random.uniform(min_value, max_value), decimals) for _ in range(size)]


def generate_arithmetic_sequence(size, start, step):
    """
    Generate an arithmetic sequence.
    
    :param size: Number of elements in the sequence.
    :param start: The starting value.
    :param step: The common difference.
    :return: List containing an arithmetic sequence.
    """
    return [start + i * step for i in range(size)]


def generate_geometric_sequence(size, start, ratio):
    """
    Generate a geometric sequence.
    
    :param size: Number of elements in the sequence.
    :param start: The starting value.
    :param ratio: The common ratio.
    :return: List containing a geometric sequence.
    """
    return [start * (ratio ** i) for i in range(size)]
