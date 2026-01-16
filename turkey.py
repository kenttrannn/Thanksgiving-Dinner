#Kent Tran, Matthew Trinh
#Group 1
#November 14, 2025
#Thanksgiving Dinner

from plate_decorator import PlateDecorator

class Turkey(PlateDecorator):
  """Decorator that adds Turkey to the plate."""

  def description(self):
    base = super().description()
    if " with " in base or " and " in base:
      return base + " and Turkey"
    else:
      return base + " with Turkey"

  def area(self):
    """Return remaining area of plate after adding Turkey."""
    return super().area() - 15

  def weight(self):
    """Return remaining weight capacity of plate after adding Turkey."""
    return super().weight() - 4

  def count(self):
    """Return number of items on plate after adding Turkey."""
    return super().count() + 1