import pytest

from kothonic.collections import List as KotlinList, list_of


# --- Iterable Methods ---


def test_filter_():
	"""Test filtering a list based on a predicate."""
	# Kotlin: fun <T> Iterable<T>.filter(predicate: (T) -> Boolean): List<T>
	my_list = list_of([1, 2, 3, 4])
	expected = list_of([2, 4])

	result = my_list.filter_(lambda x: x % 2 == 0)

	assert result == expected
	assert isinstance(result, KotlinList)


def test_map_():
	"""Test mapping elements to a new list."""
	# Kotlin: fun <T, R> Iterable<T>.map(transform: (T) -> R): List<R>
	my_list = list_of([1, 2, 3])
	expected = list_of([2, 4, 6])

	result = my_list.map_(lambda x: x * 2)

	assert result == expected
	assert isinstance(result, KotlinList)


def test_plus():
	"""Test combining two lists."""
	# Kotlin: operator fun <T> Collection<T>.plus(elements: Iterable<T>): List<T>
	my_list = list_of([1, 2])
	expected = list_of([1, 2, 3])

	result = my_list.plus(list_of([3]))
	assert result == expected
	assert isinstance(result, KotlinList)

	# Test adding a Python list
	result_py = my_list.plus([3])
	assert result_py == expected
	assert isinstance(result_py, KotlinList)


def test_all_():
	"""Test if all elements satisfy a predicate."""
	# Kotlin: fun <T> Iterable<T>.all(predicate: (T) -> Boolean): Boolean
	my_list = list_of([2, 4, 6])

	assert my_list.all_(lambda x: x % 2 == 0) is True
	assert my_list.all_(lambda x: x > 10) is False


def test_any_():
	"""Test if any element satisfies a predicate."""
	# Kotlin: fun <T> Iterable<T>.any(predicate: (T) -> Boolean): Boolean
	my_list = list_of([1, 2, 3])
	assert my_list.any_(lambda x: x % 2 == 0) is True
	assert my_list.any_(lambda x: x > 10) is False


def test_associate():
	"""Test transforming elements into a map."""
	# Kotlin: fun <T, K, V> Iterable<T>.associate(transform: (T) -> Pair<K, V>): Map<K, V>
	my_list = list_of([1, 2, 3])

	# Transform each element to a key-value pair (element, element*10)
	result = my_list.associate(lambda x: (x, x * 10))

	assert result == {1: 10, 2: 20, 3: 30}
	# Note: associate returns a Map (Kothonic Map), which inherits from dict
	assert isinstance(result, dict)


def test_average():
	"""Test calculating the average of a list of numbers."""
	# Kotlin: fun Iterable<Double>.average(): Double
	my_list = list_of([1, 2, 3, 4])
	assert my_list.average() == 2.5

	empty_list = list_of([])
	assert str(empty_list.average()) == "nan"


def test_contains():
	"""Test if a list contains an element."""
	# Kotlin: operator fun <T> Iterable<T>.contains(element: T): Boolean
	my_list = list_of([1, 2, 3])

	assert my_list.contains(2) is True
	assert my_list.contains(4) is False


def test_distinct():
	"""Test returning distinct elements."""
	# Kotlin: fun <T> Iterable[T].distinct(): List<T>
	my_list = list_of([1, 2, 2, 3])
	result = my_list.distinct()

	assert isinstance(result, KotlinList)
	# Order is not guaranteed by set, but distinct should return unique elements
	assert set(result) == {1, 2, 3}
	assert len(result) == 3


def test_drop():
	"""Test dropping the first n elements."""
	# Kotlin: fun <T> Iterable[T].drop(n: Int): List<T>
	my_list = list_of([1, 2, 3, 4])
	result = my_list.drop(2)

	assert result == list_of([3, 4])
	assert isinstance(result, KotlinList)

	assert my_list.drop(10) == list_of([])


def test_drop_last():
	"""Test dropping the last n elements."""
	# Kotlin: fun <T> List<T>.dropLast(n: Int): List<T>
	my_list = list_of([1, 2, 3, 4])
	result = my_list.drop_last(1)

	assert result == list_of([1, 2, 3])
	assert isinstance(result, KotlinList)

	assert my_list.drop_last(10) == list_of([])


def test_element_at():
	"""Test retrieving an element at a specific index."""
	# Kotlin: fun <T> Iterable[T].elementAt(index: Int): T
	my_list = list_of([10, 20, 30])
	assert my_list.element_at(1) == 20

	with pytest.raises(IndexError):
		my_list.element_at(5)


def test_element_at_or_null():
	"""Test retrieving an element or None if index out of bounds."""
	# Kotlin: fun <T> Iterable[T].elementAtOrNull(index: Int): T?
	my_list = list_of([10, 20])
	assert my_list.element_at_or_null(1) == 20
	assert my_list.element_at_or_null(5) is None


def test_element_at_or_else():
	"""Test retrieving an element or a default value if index out of bounds."""
	# Kotlin: fun <T> Iterable[T].elementAtOrElse(index: Int, defaultValue: (Int) -> T): T
	my_list = list_of([10, 20])
	assert my_list.element_at_or_else(1, lambda i: 99) == 20
	assert my_list.element_at_or_else(5, lambda i: 99) == 99


def test_find():
	"""Test finding the first element matching a predicate."""
	# Kotlin: fun <T> Iterable[T].find(predicate: (T) -> Boolean): T?
	my_list = list_of([10, 20, 30])
	assert my_list.find(lambda x: x == 20) == 20
	assert my_list.find(lambda x: x == 40) is None


def test_first():
	"""Test retrieving the first element."""
	# Kotlin: fun <T> Iterable[T].first(): T
	my_list = list_of([10, 20])
	assert my_list.first() == 10

	empty_list = list_of([])
	with pytest.raises(IndexError):
		empty_list.first()


def test_first_not_null():
	"""Test retrieving the first non-null element (Custom)."""
	# Kotlin: Custom: Returns first non-null element
	my_list = list_of([None, None, 10, 20])
	assert my_list.first_not_null() == 10

	all_null = list_of([None, None])
	assert all_null.first_not_null() is None


def test_first_or_null():
	"""Test retrieving the first element or None if empty."""
	# Kotlin: fun <T> Iterable[T].firstOrNull(): T?
	my_list = list_of([10, 20])
	assert my_list.first_or_null() == 10

	empty_list = list_of([])
	assert empty_list.first_or_null() is None


def test_flatten():
	"""Test flattening a list of iterables."""
	# Kotlin: fun <T> Iterable<Iterable<T>>.flatten(): List<T>
	nested = list_of([list_of([1]), list_of([2, 3]), list_of([4])])
	expected = list_of([1, 2, 3, 4])

	result = nested.flatten()
	assert result == expected
	assert isinstance(result, KotlinList)

	# Test with mixed Python lists inside
	nested_mixed = list_of([[1], [2, 3], [4]])
	assert nested_mixed.flatten() == expected


# --- Collection Methods ---


def test_contains_all():
	"""Test if list contains all elements from another collection."""
	# Kotlin: fun <T> Collection<T>.containsAll(elements: Collection<T>): Boolean
	my_list = list_of([1, 2, 3])

	assert my_list.contains_all(list_of([1, 2])) is True
	assert my_list.contains_all(list_of([1, 4])) is False
	assert my_list.contains_all([1, 2]) is True  # works with python iterable


def test_count_():
	"""Test counting elements."""
	# Kotlin: fun <T> Collection<T>.count(): Int
	my_list = list_of([1, 2, 3])
	assert my_list.count_() == 3

	empty_list = list_of([])
	assert empty_list.count_() == 0


def test_is_empty():
	"""Test if list is empty."""
	# Kotlin: fun <T> Collection<T>.isEmpty(): Boolean
	empty_list = list_of([])
	assert empty_list.is_empty() is True

	my_list = list_of([1])
	assert my_list.is_empty() is False


def test_is_not_empty():
	"""Test if list is not empty."""
	# Kotlin: fun <T> Collection<T>.isNotEmpty(): Boolean
	my_list = list_of([1])
	assert my_list.is_not_empty() is True

	empty_list = list_of([])
	assert empty_list.is_not_empty() is False


def test_kt_list_instance():
	"""Verify KotlinList instance behavior."""
	kt = list_of([1, 2, 3])

	# Verify it's a KotlinList instance
	assert isinstance(kt, KotlinList)
	assert isinstance(kt, list)  # It is also a list

	# Chaining example
	result = kt.filter_(lambda x: x > 1).map_(lambda x: x * 10)
	assert result == list_of([20, 30])
	assert isinstance(result, KotlinList)


def test_empty_list_factory():
	"""Test empty_list() factory function."""
	from kothonic.collections import empty_list

	e = empty_list()
	assert isinstance(e, KotlinList)
	assert len(e) == 0
	assert e.is_empty() is True


def test_list_of_factory():
	"""Test list_of() factory function."""
	kt_list = list_of([1, 2, 3])
	assert isinstance(kt_list, KotlinList)
	assert len(kt_list) == 3

	kt_list2 = list_of((1, 2))
	assert isinstance(kt_list2, KotlinList)
	assert kt_list2 == list_of([1, 2])


def test_iterable_interface_behavior():
	"""Test specific Iterable behaviors."""
	kt_list = list_of([1, 2, 3])
	iterator = iter(kt_list)
	assert next(iterator) == 1
	assert next(iterator) == 2
	assert next(iterator) == 3
	with pytest.raises(StopIteration):
		next(iterator)


def test_collection_interface_behavior():
	"""Test Collection behaviors."""
	kt_list = list_of([1, 2])
	# contains_all is a Collection method
	assert kt_list.contains_all([1]) is True
	assert kt_list.is_empty() is False
