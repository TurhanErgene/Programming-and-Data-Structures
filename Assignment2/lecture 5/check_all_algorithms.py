import pytest


exit_code = pytest.main(["test_sorting.py"])
if exit_code == 0:
    print("All sorting algorithms passed the tests!")
else:
    print("Some tests failed. Check the output above.")
