#Kent Tran, Matthew Trinh
#Group 1
#November 14, 2025
#Thanksgiving Dinner

from plate import Plate

class LargePlate(Plate):
  """Extends from Plate"""

  def description(self):
    """Returns description of plate"""
    return "Flimsy 12 inch paper plate"

  def area(self):
    """Returns area of plate"""
    return 113

  def weight(self):
    """Returns weight capacity of plate"""
    return 24

  def count(self):
    """Returns 0 (no items on plate)"""
    return 0