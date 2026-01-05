import pytest

from kothonic.collections import Set, set_of, empty_set


def test_filter_():
	s: Set[int] = set_of({1, 2, 3, 4})
	# filter_ returns a List according to Iterable
	result = s.filter_(lambda x: x % 2 == 0)
	# Sets are unordered, so result list order might vary if implementation iterates set directly.
	# But result is a List.
	assert len(result) == 2
	assert 2 in result
	assert 4 in result


def test_map_():
	s: Set[int] = set_of({1, 2, 3})
	result = s.map_(lambda x: x * 2)
	assert len(result) == 3
	assert 2 in result
	assert 4 in result
	assert 6 in result


def test_plus_variants():
	s: Set[int] = set_of({1, 2, 3})

	# Verify plus with a single element
	result1 = s.plus(4)
	assert isinstance(result1, Set)
	assert result1 == {1, 2, 3, 4}

	# Verify plus with a collection
	result2 = s.plus([4, 5])
	assert isinstance(result2, Set)
	assert result2 == {1, 2, 3, 4, 5}

	# Verify plus with a string (should be treated as single element)
	s_str: Set[str] = set_of({"a", "b"})
	result3 = s_str.plus("c")
	assert result3 == {"a", "b", "c"}
	result4 = s_str.plus("def")
	assert "def" in result4
	assert len(result4) == 3

	# Assert the original set is unmodified
	assert s == {1, 2, 3}
	assert s_str == {"a", "b"}


def test_set_specific_ops():
	s1: Set[int] = set_of({1, 2, 3})
	s2: Set[int] = set_of({3, 4, 5})

	# intersect
	intersect_res = s1.intersect(s2)
	assert isinstance(intersect_res, Set)
	assert intersect_res == {3}

	# subtract
	subtract_res = s1.subtract(s2)
	assert isinstance(subtract_res, Set)
	assert subtract_res == {1, 2}

	# Mixed Types: intersect with list
	mixed_intersect = s1.intersect([2, 3, 6])
	assert isinstance(mixed_intersect, Set)
	assert mixed_intersect == {2, 3}

	# Mixed Types: subtract with list
	mixed_subtract = s1.subtract([2, 3, 6])
	assert isinstance(mixed_subtract, Set)
	assert mixed_subtract == {1}


def test_empty_sets():
	empty = empty_set()
	s = set_of({1, 2})

	# plus
	assert empty.plus(1) == {1}
	assert s.plus(empty) == {1, 2}

	# intersect
	assert empty.intersect(s) == set()
	assert s.intersect(empty) == set()

	# subtract
	assert empty.subtract(s) == set()
	assert s.subtract(empty) == {1, 2}


def test_all_():
	s = set_of({2, 4, 6})
	assert s.all_(lambda x: x % 2 == 0) is True
	s2 = set_of({2, 3})
	assert s2.all_(lambda x: x % 2 == 0) is False


def test_any_():
	s = set_of({1, 2, 3})
	assert s.any_(lambda x: x % 2 == 0) is True
	s2 = set_of({1, 3, 5})
	assert s2.any_(lambda x: x % 2 == 0) is False


def test_associate():
	s = set_of({"a", "b"})
	result = s.associate(lambda x: (x.upper(), len(x)))
	assert result == {"A": 1, "B": 1}


def test_average():
	s = set_of({1, 2, 3, 4})
	assert s.average() == 2.5


def test_contains():
	s = set_of({1, 2, 3})
	assert s.contains(2) is True
	assert s.contains(4) is False


def test_contains_all():
	s = set_of({1, 2, 3})
	assert s.contains_all([1, 2]) is True
	assert s.contains_all([4, 5]) is False


def test_count_():
	s = set_of({1, 2, 3})
	assert s.count_() == 3


def test_distinct():
	s = set_of({1, 2, 3})
	d = s.distinct()
	assert set(d) == {1, 2, 3}


def test_drop():
	s = set_of({1, 2, 3})
	# drop returns List. Order of set iteration is not guaranteed.
	# But drop(1) should remove one element.
	result = s.drop(1)
	assert len(result) == 2


def test_drop_last():
	s = set_of({1, 2, 3})
	result = s.drop_last(1)
	assert len(result) == 2


def test_element_at():
	s = set_of({10, 20, 30})
	# element_at depends on iteration order
	result = s.element_at(0)
	assert result in {10, 20, 30}


def test_element_at_or_null():
	s = set_of({10})
	result = s.element_at_or_null(0)
	assert result == 10
	assert s.element_at_or_null(10) is None


def test_element_at_or_else():
	s = set_of({10})
	result = s.element_at_or_else(10, lambda i: 99)
	assert result == 99


def test_find():
	s = set_of({10, 20, 30})
	res = s.find(lambda x: x == 20)
	assert res == 20
	res2 = s.find(lambda x: x > 100)
	assert res2 is None


def test_first():
	s = set_of({10, 20})
	# Order undefined, but first() should return one of them
	result = s.first()
	assert result in {10, 20}


def test_first_not_null():
	s = set_of({None, 10})
	assert s.first_not_null() == 10


def test_first_or_null():
	s = set_of({10})
	assert s.first_or_null() == 10
	empty = set_of(set())
	assert empty.first_or_null() is None


def test_flatten():
	# set_of({(1, 2), (3,)})
	s2 = set_of({(1, 2), (3,)})
	flat = s2.flatten()
	assert len(flat) == 3
	assert 1 in flat
	assert 2 in flat
	assert 3 in flat


def test_is_empty():
	s = set_of(set())
	assert s.is_empty() is True
	s2 = set_of({1})
	assert s2.is_empty() is False


def test_is_not_empty():
	s = set_of({1})
	assert s.is_not_empty() is True
	s2 = set_of(set())
	assert s2.is_not_empty() is False


def test_set_instance():
	kt = set_of({1, 2, 3})
	assert isinstance(kt, Set)


def test_empty_set_factory():
	"""Test empty_set() factory function."""
	e = empty_set()
	assert isinstance(e, Set)
	assert len(e) == 0
	assert e.is_empty() is True


def test_set_of_factory():
	"""Test set_of() factory function."""
	s = set_of({1, 2})
	assert isinstance(s, Set)
	assert len(s) == 2

	s2 = set_of([1, 2])  # Iterable input
	assert isinstance(s2, Set)
	assert len(s2) == 2


if __name__ == "__main__":
	pytest.main([__file__])
