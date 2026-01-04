import builtins

from typing import Generic, TypeVar

from typing_extensions import Self


T = TypeVar("T")


class InlineValue(Generic[T]):
	"""
	A wrapper class that proxies method calls and operations to the underlying value.
	This is used to mimic Kotlin's value types or inline classes where the wrapper
	imposes minimal overhead and behaves like the wrapped value.
	"""

	__slots__ = ["value"]
	value: T

	@property
	def _kotlin_value(self) -> T:
		return self.value

	# Proxying methods to behave like the underlying object
	def __len__(self):
		return len(self.value)

	def __getitem__(self, item):
		return self.value[item]

	def __setitem__(self, key, value):
		self.value[key] = value

	def __iter__(self):
		return iter(self.value)

	def __contains__(self, item):
		return item in self.value

	def __setattr__(self, key, value):
		# Constraint 1: Restrict attribute name
		if key != "value":
			raise AttributeError(f"Cannot set attribute '{key}'. Only 'value' is allowed.")

		# Pass to the next class in the MRO (Method Resolution Order)
		super().__setattr__(key, value)

	def __init__(self, value: T):
		self.value = value

	# --- 1. Delegate attribute access (e.g., "hello".upper()) ---
	def __getattr__(self, name):
		return getattr(self.value, name)

	# --- 2. String representation ---
	def __str__(self):
		return str(self.value)

	# --- 3. Comparison Operators ---
	def __eq__(self, other):
		return self.value == (other.value if isinstance(other, InlineValue) else other)

	def __lt__(self, other):
		return self.value < (other.value if isinstance(other, InlineValue) else other)

	def __gt__(self, other):
		return self.value > (other.value if isinstance(other, InlineValue) else other)

	##
	def __add__(self, other) -> Self:
		other_val = other.value if isinstance(other, InlineValue) else other
		return self.__class__(self.value + other_val)

	def __radd__(self, other) -> Self:
		other_val = other.value if isinstance(other, InlineValue) else other
		return self.__class__(other_val + self.value)

	def __iadd__(self, other) -> Self:
		other_val = other.value if isinstance(other, InlineValue) else other
		self.value = self.value + other_val
		return self

	def __sub__(self, other) -> Self:
		other_val = other.value if isinstance(other, InlineValue) else other
		return self.__class__(self.value - other_val)

	def __rsub__(self, other) -> Self:
		other_val = other.value if isinstance(other, InlineValue) else other
		return self.__class__(other_val - self.value)

	def __isub__(self, other) -> Self:
		other_val = other.value if isinstance(other, InlineValue) else other
		self.value = self.value - other_val
		return self

	def __mul__(self, other) -> Self:
		other_val = other.value if isinstance(other, InlineValue) else other
		return self.__class__(self.value * other_val)

	def __rmul__(self, other) -> Self:
		other_val = other.value if isinstance(other, InlineValue) else other
		return self.__class__(other_val * self.value)

	def __imul__(self, other) -> Self:
		other_val = other.value if isinstance(other, InlineValue) else other
		self.value = self.value * other_val
		return self

	def __truediv__(self, other) -> Self:
		other_val = other.value if isinstance(other, InlineValue) else other
		return self.__class__(self.value / other_val)

	def __rtruediv__(self, other) -> Self:
		other_val = other.value if isinstance(other, InlineValue) else other
		return self.__class__(other_val / self.value)

	def __idiv__(self, other) -> Self:
		other_val = other.value if isinstance(other, InlineValue) else other
		self.value = self.value / other_val
		return self

	def __bool__(self):
		return bool(self.value)

	def __int__(self):
		return builtins.int(self.value)

	def __float__(self):
		return builtins.float(self.value)

	def __complex__(self):
		return complex(self.value)
