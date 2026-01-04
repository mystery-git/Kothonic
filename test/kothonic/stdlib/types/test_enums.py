from enum import auto

import pytest

from kothonic.stdlib import Enum


def test_enum_ordinal():
	class Direction(Enum):
		NORTH = auto()
		SOUTH = auto()
		EAST = auto()
		WEST = auto()

	assert Direction.NORTH.ordinal == 0
	assert Direction.SOUTH.ordinal == 1
	assert Direction.EAST.ordinal == 2
	assert Direction.WEST.ordinal == 3


def test_enum_name():
	class Color(Enum):
		RED = auto()
		GREEN = auto()

	assert Color.RED.name == "RED"
	assert Color.GREEN.name == "GREEN"


def test_enum_values():
	class State(Enum):
		IDLE = auto()
		RUNNING = auto()
		FINISHED = auto()

	values = State.values()
	assert len(values) == 3
	assert values[0] == State.IDLE
	assert values[1] == State.RUNNING
	assert values[2] == State.FINISHED
	assert values == [State.IDLE, State.RUNNING, State.FINISHED]


def test_enum_value_of():
	class Command(Enum):
		START = auto()
		STOP = auto()

	assert Command.value_of("START") == Command.START
	assert Command.value_of("STOP") == Command.STOP

	with pytest.raises(KeyError):
		Command.value_of("PAUSE")


def test_enum_ordering():
	class Priority(Enum):
		LOW = auto()
		MEDIUM = auto()
		HIGH = auto()

	assert Priority.LOW < Priority.MEDIUM
	assert Priority.MEDIUM < Priority.HIGH
	assert Priority.LOW < Priority.HIGH
	assert Priority.HIGH > Priority.LOW
	assert Priority.MEDIUM >= Priority.LOW
	assert Priority.LOW <= Priority.LOW

	# Comparisons between different enums should fail (or return NotImplemented which leads to TypeError in strict contexts or False)
	# In Python, < between incompatible types usually raises TypeError.
	class Other(Enum):
		A = auto()

	with pytest.raises(TypeError):
		_ = Priority.LOW < Other.A


def test_enum_with_constructor_and_properties():
	class Planet(Enum):
		MERCURY = (3.303e23, 2.4397e6)
		VENUS = (4.869e24, 6.0518e6)

		def __init__(self, mass, radius):
			self.mass = mass
			self.radius = radius

		@property
		def surface_gravity(self):
			G = 6.67300e-11  # noqa: N806
			return G * self.mass / (self.radius**2)

	assert Planet.MERCURY.mass == 3.303e23
	assert Planet.MERCURY.ordinal == 0
	assert Planet.VENUS.ordinal == 1
	assert Planet.MERCURY.surface_gravity is not None


def test_enum_type_enforcement():
	# All members must have the same type
	with pytest.raises(TypeError, match="Type mismatch"):

		class BadEnum(Enum):
			A = 1
			B = "string"


def test_enum_annotated_members():
	# Test members defined only by annotation (Kotlin-like enum entries without explicit values)
	# In the implementation, these use _EnumSentinel and value returns None
	class Status(Enum):
		PENDING: int
		ACTIVE: int
		COMPLETED: int

	assert Status.PENDING.ordinal == 0  # type: ignore
	assert Status.ACTIVE.ordinal == 1  # type: ignore
	assert Status.COMPLETED.ordinal == 2  # type: ignore

	assert Status.PENDING.value is None  # type: ignore
	assert Status.values() == [Status.PENDING, Status.ACTIVE, Status.COMPLETED]
