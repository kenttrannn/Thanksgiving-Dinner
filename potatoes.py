#Kent Tran, Matthew Trinh
#Group 1
#November 14, 2025
#Thanksgiving Dinner

from plate_decorator import PlateDecorator

class Potatoes(PlateDecorator):
  """Decorator that adds Potatoes to the plate."""

  def description(self):
    """Return description of plate with Potatoes."""
    base = super().description()
    if " with " in base or " and " in base:
      return base + " and Potatoes"
    else:
      return base + " with Potatoes"

  def area(self):
    """Return remaining area of plate after adding Potatoes."""
    return super().area() - 18

  def weight(self):
    """Return remaining weight capacity of plate after adding Potatoes."""
    return super().weight() - 6

  def count(self):
    """Return number of items on plate after adding Potatoes."""
    return super().count() + 1