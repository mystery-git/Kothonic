# pyrefly: ignore-errors


import pytest  # noqa: F401

from kothonic.builtins_ext import kotlin_extend  # noqa: F401


def test_list_literals():
	kotlin_extend(list)
	assert [1, 2, 3].first() == 1
	assert [1, 2, 3].filter_(lambda x: x > 1) == [2, 3]
	assert [1, 2, 3].map_(lambda x: x * 2) == [2, 4, 6]
	assert [[1], [2]].flatten() == [1, 2]


def test_dict_literals():
	kotlin_extend(dict)
	m = {"a": 1, "b": 2}
	assert m.contains_key("a") is True
	assert {"x": 10}.contains_key("x") is True
	assert {"x": 10}.contains_value(10) is True
	assert {"a": 1}.filter_(lambda entry: entry[0] == "a") == {"a": 1}


def test_set_literals():
	kotlin_extend(set)
	s = {1, 2, 3}
	assert s.contains(1) is True
	assert {1, 2}.contains(3) is False
	assert {1, 2, 3}.first() in {1, 2, 3}


def test_string_literals():
	kotlin_extend(str)
	assert "hello".uppercase() == "HELLO"
	assert "  trim  ".trim() == "trim"
	assert "123".to_int_or_null() == 123
	assert "abc".to_int_or_null() is None


def test_int_literals():
	kotlin_extend(int)
	assert (10).to_float() == 10.0
	assert (10).to_string() == "10"


def test_float_literals():
	kotlin_extend(float)
	assert (10.5).to_int() == 10
	assert (10.5).to_string() == "10.5"


def test_string_complex():
	kotlin_extend(str)
	s = "hello world"
	assert s.substring(6, len(s)) == "world"
	assert s.starts_with("hello")
	assert s.ends_with("world")
	assert s.plus("!") == "hello world!"


def test_list_complex():
	kotlin_extend(list)
	my_list = [1, 2, 3, 4]
	assert my_list.size == 4
	assert my_list.is_empty() is False
	assert my_list.contains(3)

	l2 = [1, 2]
	assert l2.plus([3, 4]) == [1, 2, 3, 4]


def test_map_complex():
	kotlin_extend(dict)
	m = {"a": 1, "b": 2}
	assert m.entries.size == 2  # Assuming entries returns a collection with size
	# Check if we can interact with keys/values as collections if implemented
	# assert m.keys.contains("a")


def test_set_complex():
	kotlin_extend(set)
	s = {1, 2, 3}
	assert s.size == 3
	assert s.contains_all([1, 2])


if __name__ == "__main__":
	pytest.main([__file__])
