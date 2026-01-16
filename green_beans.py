#Kent Tran, Matthew Trinh
#Group 1
#November 14, 2025
#Thanksgiving Dinner

from plate_decorator import PlateDecorator

class GreenBeans(PlateDecorator):
  """Decorator that adds Green Beans to the plate."""

  def description(self):
    """Return description of plate with Green Beans."""
    base = super().description()
    if " with " in base or " and " in base:
      return base + " and Green Beans"
    else:
      return base + " with Green Beans"

  def area(self):
    """Return remaining area of plate after adding Green Beans."""
    return super().area() - 20

  def weight(self):
    """Return remaining weight capacity of plate after adding Green Beans."""
    return super().weight() - 3

  def count(self):
    """Return number of items on plate after adding Green Beans."""
    return super().count() + 1