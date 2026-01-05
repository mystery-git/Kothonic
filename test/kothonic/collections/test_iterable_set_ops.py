import pytest
from kothonic.collections import list_of, set_of, Set as KotlinSet


def test_union():
	"""Test union of two collections."""
	# Kotlin: infix fun <T> Iterable<T>.union(other: Iterable<T>): Set<T>
	list1 = list_of([1, 2, 3])
	list2 = list_of([3, 4, 5])

	result = list1.union(list2)

	assert isinstance(result, KotlinSet)
	assert result == {1, 2, 3, 4, 5}

	# Test with different types
	set1 = set_of({1, 2})
	list3 = [2, 3]
	result2 = set1.union(list3)
	assert isinstance(result2, KotlinSet)
	assert result2 == {1, 2, 3}


def test_intersect():
	"""Test intersection of two collections."""
	# Kotlin: infix fun <T> Iterable<T>.intersect(other: Iterable<T>): Set<T>
	list1 = list_of([1, 2, 3])
	list2 = list_of([2, 3, 4])

	result = list1.intersect(list2)

	assert isinstance(result, KotlinSet)
	assert result == {2, 3}

	# Test with empty intersection
	list3 = [5, 6]
	result2 = list1.intersect(list3)
	assert isinstance(result2, KotlinSet)
	assert len(result2) == 0


def test_subtract():
	"""Test subtraction of two collections."""
	# Kotlin: infix fun <T> Iterable<T>.subtract(other: Iterable<T>): Set<T>
	list1 = list_of([1, 2, 3])
	list2 = list_of([2, 3, 4])

	result = list1.subtract(list2)

	assert isinstance(result, KotlinSet)
	assert result == {1}

	# Test with no overlap
	list3 = [4, 5]
	result2 = list1.subtract(list3)
	assert result2 == {1, 2, 3}
