import pytest

from kothonic import TODO


def test_todo_default():
	with pytest.raises(NotImplementedError) as exc:
		TODO()
	assert "An operation is not implemented." in str(exc.value)


def test_todo_message():
	with pytest.raises(NotImplementedError) as exc:
		TODO("Not ready yet")
	assert "Not ready yet" in str(exc.value)


def test_incomplete_function():
	def will_finish_later() -> bool:
		return TODO()

	with pytest.raises(NotImplementedError) as exc:
		will_finish_later()
	assert "An operation is not implemented." in str(exc.value)

	def custom_finish_later() -> bool:
		return TODO("Need to do X")

	with pytest.raises(NotImplementedError) as exc:
		custom_finish_later()
	assert "Need to do X" in str(exc.value)


def test_incomplete_class():
	class NotFinished:
		def will_need_this_later(self) -> float:
			return TODO()

	with pytest.raises(NotImplementedError) as exc:
		NotFinished().will_need_this_later()
	assert "An operation is not implemented." in str(exc.value)


if __name__ == "__main__":
	pytest.main([__file__])
