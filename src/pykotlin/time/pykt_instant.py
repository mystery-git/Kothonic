import builtins
from datetime import datetime
from typing import Self

a = datetime.now()

class Instant:
   def __init__(self, value: datetime):
      self.value: datetime = value

   def from_epoch_seconds(self, epoch_secs: builtins.int, nano_sec_adjust: builtins.int = 0) -> Self:
      return self

   def to_epoch_milliseconds(self):
      return self

   def parse(self, text: builtins.str) -> Self:
      self.value = datetime.fromisoformat(text)
      return self