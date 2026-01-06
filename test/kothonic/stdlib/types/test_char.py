import pytest

from kothonic.stdlib.types.char import Char
from kothonic.stdlib.types.int import Int


def test_char_creation():
	c = Char("a")
	assert c == "a"
	assert isinstance(c, Char)
	assert c.code == 97

	c2 = Char(97)
	assert c2 == "a"

	with pytest.raises(ValueError):
		Char("ab")

	with pytest.raises(ValueError):
		Char(-1)

def test_char_comparison():
	c1 = Char("a")
	c2 = Char("a")
	c3 = Char("b")

	assert c1.compare_to(c2) == 0
	assert c1.compare_to(c3) < 0
	assert c3.compare_to(c1) > 0

def test_arithmetic():
	c = Char("a")

	# plus
	assert c.plus(1) == Char("b")

	# minus
	assert c.minus(1) == Char("`")
	assert Char("b").minus(c) == 1

	# inc/dec
	assert c.inc() == Char("b")
	assert c.dec() == Char("`")

def test_conversions():
	c = Char("a") # 97

	assert c.to_int() == 97
	assert c.to_byte() == 97
	assert c.to_short() == 97
	assert c.to_long() == 97
	assert c.to_float() == 97.0
	assert c.to_double() == 97.0
	assert c.to_string() == "a"

def test_properties():
	digit = Char("1")
	letter = Char("a")
	space = Char(" ")
	upper = Char("A")

	assert digit.is_digit()
	assert not letter.is_digit()

	assert letter.is_letter()
	assert not digit.is_letter()

	assert digit.is_letter_or_digit()
	assert letter.is_letter_or_digit()
	assert not space.is_letter_or_digit()

	assert space.is_whitespace()
	assert not letter.is_whitespace()

	assert letter.is_lower_case()
	assert not letter.is_upper_case()

	assert upper.is_upper_case()
	assert not upper.is_lower_case()

def test_case_conversion():
	lower = Char("a")
	upper = Char("A")

	assert lower.to_upper_case() == upper
	assert upper.to_lower_case() == lower

def test_equals_hashcode():
	c1 = Char("a")
	c2 = Char("a")
	c3 = Char("b")

	assert c1.equals(c2)
	assert not c1.equals(c3)
	assert not c1.equals("a") # Kotlin Char equality with other types is usually false, though in Python strict typing might matter. My implementation checks isinstance(Char)

	assert c1.hash_code() == c2.hash_code()

if __name__ == "__main__":
	pytest.main([__file__])
