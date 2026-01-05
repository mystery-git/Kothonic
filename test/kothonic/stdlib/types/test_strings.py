import pytest  # noqa

from kothonic.stdlib import String


string_val: str = "test"
whole_num: int = 123
float_num: float = 123.45
test_string: String = String(string_val)
test_string_digits: String = String(str(whole_num))
test_string_float: String = String(str(float_num))


def test_kt_string():
	kt_s = String("testing")

	assert isinstance(kt_s, String)
	assert isinstance(kt_s, str)


def test_to_int():
	assert test_string_digits.to_int() == whole_num


def test_to_int_or_null():
	assert test_string_digits.to_int_or_null() == whole_num
	assert test_string.to_int_or_null() is None


def test_to_float():
	assert test_string_float.to_float() == float_num
	with pytest.raises(ValueError):
		test_string.to_float()


def test_to_float_or_null():
	assert test_string_float.to_float_or_null() == float_num
	assert test_string.to_float_or_null() is None


def test_is_null_or_empty():
	empty_string = String("")
	assert test_string.is_null_or_empty() is False
	assert empty_string.is_null_or_empty() is True
	#! TODO ("Union[T, None] should have access to is_null_or_empty and return True")


def test_is_null_or_blank():
	blank_string = String(" ")

	assert blank_string.is_null_or_blank() is True
	assert test_string.is_null_or_blank() is False
	#! TODO ("Union[T, None] should have access to is_null_or_blank and return True")


def test_reverse():
	assert test_string.reversed_() == "".join(reversed(test_string))


def test_uppercase():
	assert test_string.uppercase() == test_string.upper()


def test_lowercase():
	assert test_string.lowercase() == test_string.lower()


leading_trailing_string = String("  test  ")
leading_string = String("  test")
trailing_string = String("test  ")


def test_trim():
	assert leading_trailing_string.trim() == "test"
	assert leading_string.trim() == "test"
	assert trailing_string.trim() == "test"


def test_trim_start():
	assert leading_trailing_string.trim_start() == "test  "
	assert leading_string.trim_start() == "test"


def test_trim_end():
	assert leading_trailing_string.trim_end() == "  test"
	assert trailing_string.trim_end() == "test"


def test_substring():
	assert test_string.substring(0, 4) == test_string[0:4]


def test_contains():
	assert test_string.contains("st")


def test_starts_with():
	assert test_string.starts_with("t")
	assert not test_string.starts_with("x")


def test_ends_with():
	assert test_string.ends_with("t")
	assert not test_string.ends_with("x")


def test_capitalize():
	assert test_string.capitalize_() == test_string[0].upper() + test_string[1:]


def test_plus():
	assert test_string.plus(" world") == "test world"


def test_take():
	assert test_string.take(3) == test_string[0:3]
	assert test_string.take(10) == test_string[0:10]


def test_take_last():
	assert test_string.take_last(3) == test_string[-3:]
	assert test_string.take_last(10) == test_string[-10:]


def test_drop():
	assert test_string.drop(2) == test_string[2:]


def test_drop_last():
	assert test_string.drop_last(2) == test_string[:-2]


def test_index_of():
	assert test_string.index_of("t") == 0
	assert test_string.index_of("x") == -1
	assert test_string.index_of("s") == 2


def test_is_digit():
	assert test_string_digits.is_digit() is True
	assert test_string.is_digit() is False


def test_to_list():
	result = test_string.to_list()
	assert result == ["t", "e", "s", "t"]
	assert isinstance(result, list)


def test_method_chaining():
	new_string = test_string.uppercase().lowercase().reversed_().trim().substring(0, 2).uppercase().lowercase()
	assert new_string == "ts"


if __name__ == "__main__":
	pytest.main([__file__])
