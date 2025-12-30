import builtins
from datetime import timedelta


class Duration(timedelta):
   __SECONDS_IN_DAY = 86400
   __SECONDS_IN_HOUR = 3600
   __SECONDS_IN_MIN = 60

   def in_whole_days(self) -> builtins.int:
      return round(self.total_seconds() / self.__SECONDS_IN_DAY)

   def in_whole_hours(self) -> builtins.int:
      return round(self.total_seconds() / self.__SECONDS_IN_HOUR)

   def in_whole_minutes(self) -> builtins.int:
      return round(self.total_seconds() / self.__SECONDS_IN_MIN)

   def in_whole_seconds(self) -> builtins.int:
      return round(self.total_seconds())