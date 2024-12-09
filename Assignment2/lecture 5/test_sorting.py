import pytest
from sort_algorithms import selection_sort, bubble_sort, insertion_sort, merge_sort, quick_sort

SORT_FUNCTIONS = [
  selection_sort,
  bubble_sort,
  insertion_sort,
  merge_sort,
  quick_sort,
]

# Test cases
TEST_CASES = [
  ([5, 2, 9, 1, 5, 6], [1, 2, 5, 5, 6, 9]),
  ([], []),
  ([1], [1]),
  ([2, 1], [1, 2]),
  ([3, 3, 3], [3, 3, 3]),
  ([10, -1, 2, 5, 0, 6, 4, -5], [-5, -1, 0, 2, 4, 5, 6, 10]),
]

@pytest.mark.parametrize("sort_function", SORT_FUNCTIONS)
@pytest.mark.parametrize("input_list, expected_output", TEST_CASES)
def test_sorting_algorithms(sort_function, input_list, expected_output):
  assert sort_function(input_list) == expected_output
