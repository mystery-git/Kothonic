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
	assert test_string.starts_with("T", ignore_case=True)


def test_ends_with():
	assert test_string.ends_with("t")
	assert not test_string.ends_with("x")
	assert test_string.ends_with("T", ignore_case=True)


def test_capitalize():
	assert test_string.capitalize_() == test_string[0].upper() + test_string[1:]
	assert String("").capitalize_() == ""
	assert String("hello world").capitalize_() == "Hello world"
	assert isinstance(test_string.capitalize_(), String)


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
	from kothonic.stdlib import Int

	assert test_string.index_of("t") == 0
	assert test_string.index_of("x") == -1
	assert test_string.index_of("s") == 2
	assert test_string.index_of("T", ignore_case=True) == 0
	assert test_string.index_of("t", start_index=1) == 3
	assert isinstance(test_string.index_of("t"), Int)


def test_is_digit():
	assert test_string_digits.is_digit() is True
	assert test_string.is_digit() is False


def test_to_list():
	from kothonic.collections import List

	result = test_string.to_list()
	assert result == ["t", "e", "s", "t"]
	assert isinstance(result, List)


def test_method_chaining():
	new_string = test_string.uppercase().lowercase().reversed_().trim().substring(0, 2).uppercase().lowercase()
	assert new_string == "ts"
	assert isinstance(new_string, String)


# --- New Tests ---


def test_split():
	import re
	from kothonic.collections import List

	s = String("a,b,c")
	result = s.split_(",")
	assert result == ["a", "b", "c"]
	assert isinstance(result, List)
	assert isinstance(result[0], String)

	assert s.split_(",", limit=2) == ["a", "b,c"]

	s2 = String("a1b2c")
	assert s2.split_(re.compile(r"\d")) == ["a", "b", "c"]

	s3 = String("aAbB")
	assert s3.split_("a", ignore_case=True) == ["", "", "bB"]


def test_lines():
	from kothonic.collections import List

	s = String("a\nb\nc")
	result = s.lines()
	assert result == ["a", "b", "c"]
	assert isinstance(result, List)
	assert isinstance(result[0], String)


def test_line_sequence():
	s = String("a\nb\nc")
	seq = s.line_sequence()
	result = list(seq)
	assert result == ["a", "b", "c"]
	assert isinstance(result[0], String)


def test_replace():
	s = String("abcabc")
	result = s.replace_("a", "x")
	assert result == "xbcxbc"
	assert isinstance(result, String)
	assert s.replace_("A", "x", ignore_case=True) == "xbcxbc"


def test_replace_first():
	s = String("abcabc")
	result = s.replace_first("a", "x")
	assert result == "xbcabc"
	assert isinstance(result, String)
	assert s.replace_first("A", "x", ignore_case=True) == "xbcabc"


def test_replace_after():
	s = String("abc:def")
	result = s.replace_after(":", "xyz")
	assert result == "abc:xyz"
	assert isinstance(result, String)
	assert s.replace_after("-", "xyz", "default") == "default"


def test_replace_before():
	s = String("abc:def")
	result = s.replace_before(":", "xyz")
	assert result == "xyz:def"
	assert isinstance(result, String)
	assert s.replace_before("-", "xyz", "default") == "default"


def test_pad_start():
	s = String("abc")
	result = s.pad_start(5, "-")
	assert result == "--abc"
	assert isinstance(result, String)


def test_pad_end():
	s = String("abc")
	result = s.pad_end(5, "-")
	assert result == "abc--"
	assert isinstance(result, String)


def test_remove_prefix():
	s = String("abc")
	result = s.remove_prefix("a")
	assert result == "bc"
	assert isinstance(result, String)
	assert s.remove_prefix("x") == "abc"


def test_remove_suffix():
	s = String("abc")
	result = s.remove_suffix("c")
	assert result == "ab"
	assert isinstance(result, String)
	assert s.remove_suffix("x") == "abc"


def test_remove_range():
	s = String("abcde")
	result = s.remove_range(1, 3)
	assert result == "ade"
	assert isinstance(result, String)
	assert s.remove_range(0, 1) == "bcde"
	assert s.remove_range(4, 5) == "abcd"
	assert isinstance(s.remove_range(1, 3), String)


def test_map():
	from kothonic.collections import List

	s = String("abc")
	result = s.map_(lambda c: c.upper())
	assert result == ["A", "B", "C"]
	assert isinstance(result, List)


def test_filter():
	s = String("abc123def")
	result = s.filter_(lambda c: c.isdigit())
	assert result == "123"
	assert isinstance(result, String)


def test_for_each():
	s = String("abc")
	result = []
	s.for_each(lambda c: result.append(c))
	assert result == ["a", "b", "c"]


def test_substring_before():
	s = String("abc:def")
	result = s.substring_before(":")
	assert result == "abc"
	assert isinstance(result, String)
	assert s.substring_before("-", "default") == "default"


def test_substring_after():
	s = String("abc:def")
	result = s.substring_after(":")
	assert result == "def"
	assert isinstance(result, String)
	assert s.substring_after("-", "default") == "default"


def test_substring_before_last():
	s = String("abc:def:ghi")
	result = s.substring_before_last(":")
	assert result == "abc:def"
	assert isinstance(result, String)
	assert s.substring_before_last("-", "default") == "default"


def test_substring_after_last():
	s = String("abc:def:ghi")
	result = s.substring_after_last(":")
	assert result == "ghi"
	assert isinstance(result, String)
	assert s.substring_after_last("-", "default") == "default"


if __name__ == "__main__":
	pytest.main([__file__])
