from typing import Any


def TODO(reason: str | None = None) -> Any:  # noqa: N802
	if reason is None:
		reason = "An operation is not implemented."
	raise NotImplementedError(reason)
