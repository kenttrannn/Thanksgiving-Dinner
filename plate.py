#Kent Tran, Matthew Trinh
#Group 1
#November 14, 2025
#Thanksgiving Dinner

from abc import ABC, abstractmethod

class Plate(ABC):
  """Interface representing a plate that holds items."""
  
  @abstractmethod
  def description(self) -> str:
    """Returns a string description and what's on it."""
    pass
  
  @abstractmethod
  def area(self) -> int:
    """Returns the remaining square inches the plate can hold."""
    pass
    
  @abstractmethod
  def weight(self) -> int:
    """Returns the remaining number of ounces the plate can hold."""
    pass

  @abstractmethod
  def count(self) -> int:
    """Returns the current number of foot items the plate is holding."""
    pass