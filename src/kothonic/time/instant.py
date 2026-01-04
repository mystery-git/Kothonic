from datetime import datetime

from typing_extensions import Self


class Instant:
	def __init__(self, value: datetime):
		self.value: datetime = value

	def from_epoch_seconds(self, epoch_secs: int, nano_sec_adjust: int = 0) -> Self:
		return self

	def to_epoch_milliseconds(self):
		return self

	def parse(self, text: str) -> Self:
		self.value = datetime.fromisoformat(text)
		return self
