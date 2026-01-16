#Kent Tran, Matthew Trinh
#Group 1
#November 14, 2025
#Thanksgiving Dinner

from abc import ABC
from plate import Plate

class PlateDecorator(Plate, ABC):

  def __init__(self, p):
    """Initialize with a plate"""
    self._plate = p

  def description(self) -> str:
    """Return description of plate"""
    return self._plate.description()

  def area(self) -> int:
    """Return remaining area of plate"""
    return self._plate.area()

  def weight(self) -> int:
    """Return remaining weight capacity of plate"""
    return self._plate.weight()

  def count(self) -> int:
    """Return number of items on plate"""
    return self._plate.count()