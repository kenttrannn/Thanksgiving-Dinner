#Kent Tran, Matthew Trinh
#Group 1
#November 14, 2025
#Thanksgiving Dinner

from plate_decorator import PlateDecorator

class Stuffing(PlateDecorator):
  """Decorator that adds Stuffing to the plate."""

  def description(self):
    base = super().description()
    if " with " in base or " and " in base:
      return base + " and Stuffing"
    else:
      return base + " with Stuffing"

  def area(self):
    """Return remaining area of plate after adding Stuffing."""
    return super().area() - 18

  def weight(self):
    """Return remaining weight capacity of plate after adding Stuffing."""
    return super().weight() - 7

  def count(self):
    """Return number of items on plate after adding Stuffing."""
    return super().count() + 1