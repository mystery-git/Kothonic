import dataclasses

from dataclasses import dataclass

import pytest

from kothonic.core_features import Data


class User(Data):
	name: str
	age: int


def test_data_is_dataclass():
	u = User(name="Alice", age=30)
	assert dataclasses.is_dataclass(u)
	assert u.name == "Alice"
	assert u.age == 30


def test_data_is_frozen():
	u = User(name="Alice", age=30)
	with pytest.raises(dataclasses.FrozenInstanceError):
		u.age = 31  # type: ignore


def test_data_copy():
	u1 = User(name="Alice", age=30)
	u2 = u1.copy(age=31)

	assert u2.name == "Alice"
	assert u2.age == 31
	assert u1.age == 30  # Original should be unchanged
	assert u1 is not u2


def test_data_repr():
	u = User(name="Alice", age=30)
	assert repr(u) == "User(name='Alice', age=30)"


def test_data_equality():
	u1 = User(name="Alice", age=30)
	u2 = User(name="Alice", age=30)
	u3 = User(name="Bob", age=25)

	assert u1 == u2
	assert u1 != u3


def test_nested_inheritance():
	# Standard dataclasses
	@dataclass
	class A:
		aval: int

	@dataclass
	class B(A):
		bval: str

	b = B(aval=1, bval="hello")
	assert dataclasses.is_dataclass(b)
	assert b.aval == 1
	assert b.bval == "hello"

	print("Regular decorator makes inheritees also a dataclass")

	class Employee(User):
		role: str

	e = Employee(name="Bob", age=40, role="Dev")
	assert dataclasses.is_dataclass(e)
	assert e.name == "Bob"
	assert e.role == "Dev"

	e2 = e.copy(role="Manager")
	assert e2.role == "Manager"
	assert e2.name == "Bob"


def test_copy_replaces_variable():
	u1 = User(name="Alice", age=30)
	u2 = u1.copy(name="Bob")
	assert u2.name == "Bob"
	assert u1.name == "Alice"

	u1 = u1.copy(name="Richard")
	assert u1.name == "Richard"


def test_data_with_complex_literals():
	class Config(Data):
		items: list
		settings: dict
		flags: set

	c = Config(items=[1, 2], settings={"a": 1}, flags={1, 2})
	assert c.items == [1, 2]
	assert c.settings == {"a": 1}
	assert c.flags == {1, 2}

	# Verify standard behaviors
	c2 = c.copy()
	assert c2 == c
	assert c2 is not c


def test_pure_copy():
	u1 = User(name="Alice", age=30)
	u2 = u1.copy()
	assert u2 == u1
	assert u2 is not u1
	assert u2.name == "Alice"
	assert u2.age == 30


def test_copy_with_mutable_field():
	class Container(Data):
		data: list

	orig_list = [1, 2, 3]
	c1 = Container(data=orig_list)
	c2 = c1.copy()

	# Verify shallow copy behavior (standard in Python data classes/copy)
	assert c2.data is c1.data
	assert c2.data == [1, 2, 3]

	# Modifying the list in one should reflect in the other
	c1.data.append(4)
	assert c2.data == [1, 2, 3, 4]


def test_copy_invalid_args():
	u = User(name="Alice", age=30)

	# copy() should raise TypeError if unknown arguments are passed
	# This depends on implementation, standard dataclasses replace() raises TypeError
	with pytest.raises(TypeError):
		u.copy(unknown_field=123)


if __name__ == "__main__":
	pytest.main([__file__])
