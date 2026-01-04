import builtins

from kothonic.core_features import KotlinValue


class Char(builtins.str, KotlinValue[builtins.str]):
	def __new__(cls, value: str | int):
		if isinstance(value, int):
			if not (0 <= value <= 0x10FFFF):
				raise ValueError(f"Char code point out of range: {value}")
			return super().__new__(cls, chr(value))
		else:
			if len(value) != 1:
				raise ValueError(f"Char has a length of one, not {len(value)}")
			return super().__new__(cls, value)

	@property
	def code(self) -> int:
		return ord(self)

	# TODO("Add Kotlin's 'Char' methods here")
