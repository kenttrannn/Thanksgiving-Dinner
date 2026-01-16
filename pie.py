#Kent Tran, Matthew Trinh
#Group 1
#November 14, 2025
#Thanksgiving Dinner

from plate_decorator import PlateDecorator

class Pie(PlateDecorator):
  """Decorator that adds a pie to the plate."""

  def description(self):
    """Return description of plate with pie."""
    base = super().description()
    if " with " in base or " and " in base:
      return base + " and Pie"
    else:
      return base + " with Pie"

  def area(self):
    """Return remaining area of plate after adding pie."""
    return super().area() - 19

  def weight(self):
    """Return remaining weight capacity of plate after adding pie."""
    return super().weight() - 8

  def count(self):
    """Return number of items on plate after adding pie."""
    return super().count() + 1