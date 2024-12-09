import pytest
from Deque import Deque

def test_add_last():
    deque = Deque()
    deque.add_last(10)
    deque.add_last(20)
    deque.add_last(30)

    assert str(deque) == "{ 10 20 30 }"
    assert deque.size == 3
    assert deque.get_last() == 30
    assert deque.get_first() == 10

def test_add_first():
    deque = Deque()
    deque.add_first(10)
    deque.add_first(20)
    deque.add_first(30)

    assert str(deque) == "{ 30 20 10 }"
    assert deque.size == 3
    assert deque.get_first() == 30
    assert deque.get_last() == 10

def test_remove_first():
    deque = Deque()
    deque.add_last(10)
    deque.add_last(20)
    deque.add_last(30)

    assert deque.remove_first() == 10
    assert deque.remove_first() == 20
    assert deque.size == 1
    assert deque.remove_first() == 30
    assert deque.is_empty()

    # Test removing from an empty deque
    with pytest.raises(IndexError):
        deque.remove_first()

def test_remove_last():
    deque = Deque()
    deque.add_last(10)
    deque.add_last(20)
    deque.add_last(30)

    assert deque.remove_last() == 30
    assert deque.remove_last() == 20
    assert deque.size == 1
    assert deque.remove_last() == 10
    assert deque.is_empty()

    # Test removing from an empty deque
    with pytest.raises(IndexError):
        deque.remove_last()

def test_get_first_and_last():
    deque = Deque()
    deque.add_last(10)
    deque.add_last(20)
    deque.add_last(30)

    assert deque.get_first() == 10
    assert deque.get_last() == 30

    deque.add_first(5)
    assert deque.get_first() == 5
    deque.add_last(40)
    assert deque.get_last() == 40

    # Test accessing an empty deque
    empty_deque = Deque()
    with pytest.raises(IndexError):
        empty_deque.get_first()
    with pytest.raises(IndexError):
        empty_deque.get_last()

def test_is_empty():
    deque = Deque()
    assert deque.is_empty()

    deque.add_last(10)
    assert not deque.is_empty()

    deque.remove_first()
    assert deque.is_empty()

def test_iteration():
    deque = Deque()
    for i in range(1, 6):  # Add elements 1 to 5
        deque.add_last(i)

    elements = list(deque)
    assert elements == [1, 2, 3, 4, 5]

def test_add_and_remove_all():
    deque = Deque()
    for i in range(1, 101):  # Add elements 1 to 100
        deque.add_last(i)

    assert deque.size == 100
    assert deque.get_first() == 1
    assert deque.get_last() == 100

    for i in range(1, 101):  # Remove all elements
        assert deque.remove_first() == i

    assert deque.is_empty()

    # Verify empty state
    assert str(deque) == "{ }"
    assert deque.size == 0
    with pytest.raises(IndexError):
        deque.get_first()
    with pytest.raises(IndexError):
        deque.get_last()

def test_edge_cases():
    deque = Deque()

    # Add and remove a single element
    deque.add_last(10)
    assert deque.get_first() == 10
    assert deque.get_last() == 10
    assert deque.remove_first() == 10
    assert deque.is_empty()

    # Add and remove with add_first
    deque.add_first(20)
    assert deque.get_first() == 20
    assert deque.get_last() == 20
    assert deque.remove_last() == 20
    assert deque.is_empty()
