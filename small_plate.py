#Kent Tran, Matthew Trinh
#Group 1
#November 14, 2025
#Thanksgiving Dinner

from plate import Plate

class SmallPlate(Plate):
  """Extends from Plate"""
  
  def description(self):
    """Returns description of plate"""
    return "Sturdy 10 inch paper plate"

  def area(self):
    """Returns area of plate"""
    return 78

  def weight(self):
    """Returns weight capacity of plate"""
    return 32

  def count(self):
    """Returns 0 (no items on plate)"""
    return 0
  