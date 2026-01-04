from kothonic.collections import Map, List, map_of


def test_map_creation():
	m = map_of({"a": 1, "b": 2})
	assert isinstance(m, Map)
	assert isinstance(m, dict)
	assert m["a"] == 1
	assert len(m) == 2


def test_contains_key():
	m = map_of({"a": 1, "b": 2})
	assert m.contains_key("a") is True
	assert m.contains_key("z") is False


def test_contains_value():
	m = map_of({"a": 1, "b": 2})
	assert m.contains_value(1) is True
	assert m.contains_value(3) is False


def test_collection_methods():
	m = map_of({"a": 1, "b": 2})

	# is_empty / is_not_empty
	assert m.is_empty() is False
	assert m.is_not_empty() is True
	assert map_of({}).is_empty() is True

	# count_
	assert m.count_() == 2

	# contains_all (checks keys)
	assert m.contains_all(["a", "b"]) is True
	assert m.contains_all(["a", "c"]) is False


def test_iterable_methods_operate_on_keys():
	# Since Map inherits Collection[K], it behaves like an Iterable of keys for some methods
	m = map_of({"a": 1, "b": 2})

	# all_ / any_
	assert m.all_(lambda k: len(k) == 1) is True
	assert m.any_(lambda k: k == "b") is True

	# contains
	assert m.contains("a") is True

	# first / first_or_null
	# Dict order is preserved in recent Python versions
	assert m.first() == "a"
	assert map_of({}).first_or_null() is None


def test_map_specific_methods():
	m = map_of({"a": 1, "b": 2})

	# filter_ (now operates on entries and returns Map)
	filtered = m.filter_(lambda entry: entry[1] == 1)
	assert isinstance(filtered, Map)
	assert filtered == {"a": 1}

	# filter_keys
	filtered_keys = m.filter_keys(lambda k: k == "a")
	assert isinstance(filtered_keys, Map)
	assert filtered_keys == {"a": 1}

	# filter_values
	filtered_values = m.filter_values(lambda v: v == 2)
	assert isinstance(filtered_values, Map)
	assert filtered_values == {"b": 2}

	# map_ (now operates on entries)
	mapped = m.map_(lambda entry: f"{entry[0]}{entry[1]}")
	assert isinstance(mapped, List)
	assert mapped == ["a1", "b2"]


def test_plus_map_behavior():
	# plus on Map now returns a merged Map
	m1 = map_of({"a": 1})
	m2 = map_of({"b": 2})

	result = m1.plus(m2)
	assert isinstance(result, Map)
	assert result == {"a": 1, "b": 2}

	# Test with iterable of pairs
	result2 = m1.plus([("c", 3)])
	assert isinstance(result2, Map)
	assert result2 == {"a": 1, "c": 3}


def test_associate():
	# associate transforms keys into a new Map
	m = map_of({"a": 1, "b": 2})

	# Example: Create map where key is upper case of original key, and value is original value * 10
	# Note: access m[k] is required if we want the value
	result = m.associate(lambda k: (k.upper(), m[k] * 10))

	assert isinstance(result, Map)
	assert result == {"A": 10, "B": 20}


def test_average():
	# Only works if keys are numbers
	m = map_of({1: "a", 3: "b"})
	assert m.average() == 2.0


def test_distinct():
	# Keys are already distinct, but returns List
	m = map_of({"a": 1, "b": 2})
	distinct_keys = m.distinct()
	assert isinstance(distinct_keys, List)
	assert len(distinct_keys) == 2
	assert "a" in distinct_keys
	assert "b" in distinct_keys


def test_drop_and_take():
	# drop/drop_last
	m = map_of({"a": 1, "b": 2, "c": 3})

	dropped = m.drop(1)
	assert dropped == ["b", "c"]

	dropped_last = m.drop_last(1)
	assert dropped_last == ["a", "b"]


def test_element_at():
	m = map_of({"a": 1, "b": 2})
	assert m.element_at(0) == "a"
	assert m.element_at_or_null(5) is None
	assert m.element_at_or_else(5, lambda i: "default") == "default"


def test_find():
	m = map_of({"a": 1, "b": 2})
	assert m.find(lambda k: k == "b") == "b"
	assert m.find(lambda k: k == "z") is None


def test_first_not_null():
	# If keys contain None and we want first non-None
	# Note: Using tuple as keys because list is unhashable, but None is hashable
	m = map_of({None: 1, "a": 2})
	# Since dict order is insertion order:
	assert m.first_not_null() == "a"


def test_flatten():
	# If keys are iterables (like tuples)
	m = map_of({(1, 2): "a", (3,): "b"})
	# flatten operates on keys
	flat = m.flatten()
	assert isinstance(flat, List)
	assert len(flat) == 3
	assert 1 in flat
	assert 2 in flat
	assert 3 in flat


def test_empty_map_factory():
	"""Test empty_map() factory function."""
	from kothonic.collections import empty_map

	e = empty_map()
	assert isinstance(e, Map)
	assert len(e) == 0
	assert e.is_empty() is True


def test_map_of_factory():
	"""Test map_of() factory function."""
	m = map_of({"a": 1})
	assert isinstance(m, Map)
	assert m["a"] == 1

	m2 = map_of({})
	assert isinstance(m2, Map)
	assert m2.is_empty() is True
