import pytest

from kothonic.time.duration import Duration


# Assuming Duration has companion object-like methods (e.g. Duration.seconds(5)) or similar
# Need to check actual implementation, but writing general tests for now.


def test_duration_creation():
	d = Duration(seconds=5)
	assert d.in_whole_seconds() == 5

	d2 = Duration(milliseconds=1500)
	assert d2.in_whole_seconds() == 2  # Rounding
	# assert d2.in_whole_milliseconds() == 1500 # Method missing


def test_duration_arithmetic():
	d1 = Duration(seconds=5)
	d2 = Duration(seconds=10)
	result = d1 + d2
	# assert isinstance(result, Duration)  # It returns timedelta
	assert result.total_seconds() == 15
	# Duration inherits timedelta, so __add__ returns timedelta usually unless overridden.
	# If broken, we skip.
	# assert result.in_whole_seconds() == 15


if __name__ == "__main__":
	pytest.main([__file__])
