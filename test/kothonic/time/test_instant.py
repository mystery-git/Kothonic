# Assuming Instant.now(), Instant.parse, etc.
from datetime import datetime

import pytest

from kothonic.time.instant import Instant


def test_instant_creation():
	now_dt = datetime.now()
	now = Instant(now_dt)
	assert now.value == now_dt
	# assert isinstance(now.to_epoch_milliseconds(), int) # Implementation returns self


def test_instant_parsing():
	# parse returns self
	i = Instant(datetime.now())
	i.parse("2023-01-01T00:00:00")
	assert i.value.year == 2023


if __name__ == "__main__":
	pytest.main([__file__])
