import pytest

from kothonic import assert_


def test_assert_pass():
	assert_(True)
	assert_(True, lambda: "Should not be called")


def test_assert_fail():
	with pytest.raises(AssertionError):
		assert_(False)
	with pytest.raises(AssertionError):
		assert_(False)


def test_assert_fail_with_message():
	with pytest.raises(AssertionError) as exc:
		assert_(False, lambda: "Custom assert message")
	assert "Custom assert message" in str(exc.value)


if __name__ == "__main__":
	pytest.main([__file__])
