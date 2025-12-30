import builtins

from numpy import random


class Random:
   def __init__(self, seed: builtins.int):
      self.__seed = seed

   @staticmethod
   def next_int() -> builtins.int:
      return random.randint(low = 0)