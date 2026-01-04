import pytest

from kothonic import IllegalStateException, check, check_not_null


def test_check_pass():
	check(True)
	check(True, lambda: "Should not be called")


def test_check_fail():
	with pytest.raises(IllegalStateException):
		check(False)


def test_check_fail_with_message():
	with pytest.raises(IllegalStateException) as exc:
		check(False, lambda: "Custom message")
	assert "Custom message" in str(exc.value)


def test_check_not_null_pass():
	val = "not null"
	result = check_not_null(val)
	assert result == "not null"


def test_check_not_null_fail():
	with pytest.raises(IllegalStateException):
		check_not_null(None)


def test_check_not_null_fail_with_message():
	with pytest.raises(IllegalStateException) as exc:
		check_not_null(None, lambda: "Custom null message")
	assert "Custom null message" in str(exc.value)


if __name__ == "__main__":
	pytest.main([__file__])
