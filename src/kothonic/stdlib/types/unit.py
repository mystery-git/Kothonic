from .string import String


class UnitType:
	"""Behaves like Kotlin's Unit type."""

	_instance = None

	def __new__(cls):
		# Ensures only one instance ever exists (Singleton)
		if cls._instance is None:
			cls._instance = super().__new__(cls)
		return cls._instance

	def to_string(self) -> String:
		return String(str(self))

	def __repr__(self):
		return "Unit"

	def __bool__(self):
		return False


# Create the global constant
Unit = UnitType()
