from __future__ import annotations

import re
import builtins

from typing import TYPE_CHECKING, Any
from collections.abc import Callable, Iterable

from kothonic.core_features import KotlinValue


if TYPE_CHECKING:
	from kothonic.collections import List

	from .int import Int
	from .float import Float


class String(str, KotlinValue[str]):
	"""
	A Kotlin-style string that extends Python's built-in str with additional functional methods.

	This class provides Kotlin-like operations such as to_int(), to_float(), trim(), substring(), and more, while maintaining full compatibility with Python's standard str type.
	"""

	@property
	def _kotlin_value(self) -> String:
		return self

	# Kotlin: fun String.toInt(): Int
	def to_int(self) -> Int:
		"""Parses the string as an Int number and returns the result."""
		from .int import Int

		return Int(int(self))

	# Kotlin: fun String.toIntOrNull(): Int?
	def to_int_or_null(self) -> Int | None:
		"""Parses the string as an Int number and returns the result or null if the string is not a valid representation of a number."""
		from .int import Int

		try:
			return Int(int(self))
		except Exception:
			return None

	# Kotlin: fun String.toFloat(): Float
	def to_float(self) -> Float:
		"""Parses the string as a Float number and returns the result."""
		from .float import Float

		return Float(float(self))

	# Kotlin: fun String.toFloatOrNull(): Float?
	def to_float_or_null(self) -> Float | None:
		"""Parses the string as a Float number and returns the result or null if the string is not a valid representation of a number."""
		from .float import Float

		try:
			return Float(float(self))
		except ValueError:
			return None

	# Kotlin: fun String?.isNullOrEmpty(): Boolean
	def is_null_or_empty(self) -> bool:
		"""Returns true if this char sequence is null or empty."""
		# TODO("Known issue: self is None is unreachable in instance methods. This will be addressed when implementing nullable types properly.")
		return self is None or self == ""

	# Kotlin: fun String?.isNullOrBlank(): Boolean
	def is_null_or_blank(self) -> bool:
		"""Returns true if this char sequence is null or empty or consists solely of whitespace characters."""
		# TODO("Known issue: self is None is unreachable in instance methods. This will be addressed when implementing nullable types properly.")
		return self is None or self.strip().replace(" ", "") == ""

	# Kotlin: fun String.reversed(): String
	def reversed_(self) -> String:
		"""Returns a sequence with characters in reversed order."""
		return String("".join(builtins.reversed(self)))

	# Kotlin: fun String.uppercase(): String
	def uppercase(self) -> String:
		"""Returns a copy of this string converted to upper case using the rules of the default locale."""
		return String(self.upper())

	# Kotlin: fun String.lowercase(): String
	def lowercase(self) -> String:
		"""Returns a copy of this string converted to lower case using the rules of the default locale."""
		return String(self.lower())

	# Kotlin: fun String.trim(): String
	def trim(self) -> String:
		"""Returns a string having leading and trailing whitespace removed."""
		return String(self.strip())

	# Kotlin: fun String.trimStart(): String
	def trim_start(self) -> String:
		"""Returns a string having leading whitespace removed."""
		return String(self.lstrip())

	# Kotlin: fun String.trimEnd(): String
	def trim_end(self) -> String:
		"""Returns a string having trailing whitespace removed."""
		return String(self.rstrip())

	# Kotlin: fun String.substring(startIndex: Int, endIndex: Int): String
	def substring(self, start: int, end: int) -> String:
		"""Returns a substring of this string that starts at the specified startIndex and continues to the index before endIndex."""
		return String(self[start:end])

	# Kotlin: operator fun String.contains(other: String): Boolean
	def contains(self, match: str) -> bool:
		"""Returns true if this string contains the other as a substring."""
		return match in self

	# Kotlin: fun String.startsWith(prefix: String, ignoreCase: Boolean = false): Boolean
	def starts_with(self, prefix: str, ignore_case: bool = False) -> bool:
		"""Returns true if this string starts with the specified prefix."""
		prefix = prefix.lower() if ignore_case else prefix
		compare_to = self.lower() if ignore_case else self
		return compare_to.startswith(prefix)

	# Kotlin: fun String.endsWith(suffix: String, ignoreCase: Boolean = false): Boolean
	def ends_with(self, suffix: str, ignore_case: bool = False) -> bool:
		"""Returns true if this string ends with the specified suffix."""
		suffix_check = suffix.lower() if ignore_case else suffix
		compare_to = self.lower() if ignore_case else self
		return compare_to.endswith(suffix_check)

	# Kotlin: operator fun String.plus(other: Any?): String
	def plus(self, other: Any) -> String:
		"""Returns the concatenation of this string with the string representation of the given other object."""
		return String(self + str(other))

	# Kotlin: fun String.capitalize(): String
	def capitalize_(self) -> String:
		"""Returns a copy of this string having its first letter titlecased, or the original string if it's empty or already starts with a title case letter."""
		if not self:
			return self
		return String(self[0].upper() + self[1:])

	# Kotlin: fun String.take(n: Int): String
	def take(self, n: int) -> String:
		"""Returns a string containing the first n characters."""
		return String(self[:n])

	# Kotlin: fun String.takeLast(n: Int): String
	def take_last(self, n: int) -> String:
		"""Returns a string containing the last n characters."""
		length = len(self)
		return String(self[(length - n) :])

	# Kotlin: fun String.drop(n: Int): String
	def drop(self, n: int) -> String:
		"""Returns a string with the first n characters removed."""
		return String(self[n:])

	# Kotlin: fun String.dropLast(n: Int): String
	def drop_last(self, n: int) -> String:
		"""Returns a string with the last n characters removed."""
		length = len(self)
		return String(self[: (length - n)])

	# Kotlin: fun String.indexOf(string: String, startIndex: Int = 0, ignoreCase: Boolean = false): Int
	def index_of(self, string: str, start_index: int = 0, ignore_case: bool = False) -> Int:
		"""Returns the index within this string of the first occurrence of the specified string."""
		from .int import Int

		if ignore_case:
			return Int(self.lower().find(string.lower(), start_index))
		return Int(self.find(string, start_index))

	# Kotlin: fun Char.isDigit(): Boolean
	def is_digit(self) -> bool:
		"""Returns true if this string consists only of digits."""
		return self.isdigit()

	# Kotlin: fun String.toList(): List<Char>
	def to_list(self) -> List:
		"""Returns a List containing all characters."""
		from kothonic.collections import List

		return List(list(self))

	# --- Splitting & Joining ---

	# Kotlin: fun CharSequence.split(regex: Regex, limit: Int = 0): List<String>
	# Kotlin: fun CharSequence.split(vararg delimiters: String, ignoreCase: Boolean = false, limit: Int = 0): List<String>
	def split_(self, delimiter: str | re.Pattern, limit: int = 0, ignore_case: bool = False) -> List[String]:
		"""Splits this string to a list of strings around occurrences of the specified delimiter."""
		from kothonic.collections import List

		if limit == 1:
			return List([self])

		maxsplit = limit - 1 if limit > 0 else -1

		if isinstance(delimiter, re.Pattern):
			re_maxsplit = maxsplit if limit > 0 else 0
			return List([String(s) for s in delimiter.split(self, maxsplit=re_maxsplit)])

		if ignore_case:
			# If ignore case is needed for string delimiter, we use regex with ignore case flag
			pattern = re.escape(delimiter)
			re_maxsplit = maxsplit if limit > 0 else 0
			return List([String(s) for s in re.split(pattern, self, maxsplit=re_maxsplit, flags=re.IGNORECASE)])

		return List([String(s) for s in self.split(delimiter, maxsplit)])

	# Kotlin: fun CharSequence.lines(): List<String>
	def lines(self) -> List[String]:
		"""Splits this char sequence to a list of lines delimited by any of the standard line terminators."""
		from kothonic.collections import List

		return List([String(s) for s in self.splitlines()])

	# Kotlin: fun CharSequence.lineSequence(): Sequence<String>
	def line_sequence(self) -> Iterable[String]:
		"""Returns a sequence of lines delimited by any of the standard line terminators."""
		return (String(s) for s in self.splitlines())

	# --- Replacement ---

	# Kotlin: fun String.replace(oldValue: String, newValue: String, ignoreCase: Boolean = false): String
	def replace_(self, old: str, new: str, ignore_case: bool = False) -> String:
		"""Returns a new string with all occurrences of old replaced by new."""
		if ignore_case:
			pattern = re.compile(re.escape(old), re.IGNORECASE)
			return String(pattern.sub(new, self))
		return String(self.replace(old, new))

	# Kotlin: fun String.replaceFirst(oldValue: String, newValue: String, ignoreCase: Boolean = false): String
	def replace_first(self, old: str, new: str, ignore_case: bool = False) -> String:
		"""Returns a new string with the first occurrence of old replaced by new."""
		if ignore_case:
			pattern = re.compile(re.escape(old), re.IGNORECASE)
			return String(pattern.sub(new, self, count=1))
		return String(self.replace(old, new, 1))

	# Kotlin: fun String.replaceAfter(delimiter: String, replacement: String, missingDelimiterValue: String = this): String
	def replace_after(self, delimiter: str, replacement: str, missing_delimiter_value: str | None = None) -> String:
		"""Returns a string with the part after the first occurrence of the delimiter replaced by the replacement string."""
		index = self.find(delimiter)
		if index == -1:
			return String(missing_delimiter_value) if missing_delimiter_value is not None else self
		return String(self[: index + len(delimiter)] + replacement)

	# Kotlin: fun String.replaceBefore(delimiter: String, replacement: String, missingDelimiterValue: String = this): String
	def replace_before(self, delimiter: str, replacement: str, missing_delimiter_value: str | None = None) -> String:
		"""Returns a string with the part before the first occurrence of the delimiter replaced by the replacement string."""
		index = self.find(delimiter)
		if index == -1:
			return String(missing_delimiter_value) if missing_delimiter_value is not None else self
		return String(replacement + self[index:])

	# --- Padding ---

	# Kotlin: fun String.padStart(length: Int, padChar: Char = ' '): String
	def pad_start(self, length: int, pad_char: str = " ") -> String:
		"""Returns a string of length at least length consisting of this string prepended with padChar as many times as are necessary to reach that length."""
		return String(self.rjust(length, pad_char))

	# Kotlin: fun String.padEnd(length: Int, padChar: Char = ' '): String
	def pad_end(self, length: int, pad_char: str = " ") -> String:
		"""Returns a string of length at least length consisting of this string appended with padChar as many times as are necessary to reach that length."""
		return String(self.ljust(length, pad_char))

	# --- Removal ---

	# Kotlin: fun String.removePrefix(prefix: CharSequence): String
	def remove_prefix(self, prefix: str) -> String:
		"""If this string starts with the given prefix, returns a copy of this string with the prefix removed. Otherwise, returns this string."""
		if self.startswith(prefix):
			return String(self[len(prefix) :])
		return self

	# Kotlin: fun String.removeSuffix(suffix: CharSequence): String
	def remove_suffix(self, suffix: str) -> String:
		"""If this string ends with the given suffix, returns a copy of this string with the suffix removed. Otherwise, returns this string."""
		if self.endswith(suffix):
			return String(self[: len(self) - len(suffix)])
		return self

	# Kotlin: fun String.removeRange(startIndex: Int, endIndex: Int): String
	def remove_range(self, start_index: int, end_index: int) -> String:
		"""Returns a string with the sub-sequence of characters from the range [startIndex, endIndex) removed."""
		return String(self[:start_index] + self[end_index:])

	# --- Functional Ops ---

	# Kotlin: inline fun <R> CharSequence.map(transform: (Char) -> R): List<R>
	def map_(self, transform: Callable[[str], Any]) -> List[Any]:
		"""Returns a list containing the results of applying the given transform function to each character in the original char sequence."""
		from kothonic.collections import List

		return List([transform(char) for char in self])

	# Kotlin: inline fun String.filter(predicate: (Char) -> Boolean): String
	def filter_(self, predicate: Callable[[str], bool]) -> String:
		"""Returns a string containing only those characters from the original string that match the given predicate."""
		return String("".join([char for char in self if predicate(char)]))

	# Kotlin: inline fun CharSequence.forEach(action: (Char) -> Unit): Unit
	def for_each(self, action: Callable[[str], None]) -> None:
		"""Performs the given action on each character."""
		for char in self:
			action(char)

	# --- Substrings ---

	# Kotlin: fun String.substringBefore(delimiter: String, missingDelimiterValue: String = this): String
	def substring_before(self, delimiter: str, missing_delimiter_value: str | None = None) -> String:
		"""Returns a string containing the characters before the first occurrence of the delimiter."""
		index = self.find(delimiter)
		if index == -1:
			return String(missing_delimiter_value) if missing_delimiter_value is not None else self
		return String(self[:index])

	# Kotlin: fun String.substringAfter(delimiter: String, missingDelimiterValue: String = this): String
	def substring_after(self, delimiter: str, missing_delimiter_value: str | None = None) -> String:
		"""Returns a string containing the characters after the first occurrence of the delimiter."""
		index = self.find(delimiter)
		if index == -1:
			return String(missing_delimiter_value) if missing_delimiter_value is not None else self
		return String(self[index + len(delimiter) :])

	# Kotlin: fun String.substringBeforeLast(delimiter: String, missingDelimiterValue: String = this): String
	def substring_before_last(self, delimiter: str, missing_delimiter_value: str | None = None) -> String:
		"""Returns a string containing the characters before the last occurrence of the delimiter."""
		index = self.rfind(delimiter)
		if index == -1:
			return String(missing_delimiter_value) if missing_delimiter_value is not None else self
		return String(self[:index])

	# Kotlin: fun String.substringAfterLast(delimiter: String, missingDelimiterValue: String = this): String
	def substring_after_last(self, delimiter: str, missing_delimiter_value: str | None = None) -> String:
		"""Returns a string containing the characters after the last occurrence of the delimiter."""
		index = self.rfind(delimiter)
		if index == -1:
			return String(missing_delimiter_value) if missing_delimiter_value is not None else self
		return String(self[index + len(delimiter) :])
