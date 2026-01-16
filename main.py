#Kent Tran, Matthew Trinh
#Group 5
#November 14, 2025
#Thanksgiving Dinner

import check_input
from small_plate import SmallPlate
from large_plate import LargePlate
from turkey import Turkey
from stuffing import Stuffing
from potatoes import Potatoes
from green_beans import GreenBeans
from pie import Pie

def examine_plate(p):
  """Print description, area, weight, and count of plate."""
  print(p.description())

  if p.area() <= 0 or p.weight() <= 0:
    if p.area() <= 0:
      print("Your plate isn't big enough for this much food! Your food spills all over the edge.")
    else:
      print("Your plate bends under the weight of your food. Your food spills on the floor.")
    return True

  weight_remaining = p.weight()
  if 1<= weight_remaining <= 6:
    sturdiness = "Bending"
  elif 7 <= weight_remaining <= 12:
    sturdiness = "weak"
  else:
    sturdiness = "Strong"

  print(f"Sturdiness: {sturdiness}")

  area_remaining = p.area()
  if 1 <= area_remaining <= 20:
    space = "A tiny bit"
  elif 21 <= area_remaining <= 40:
    space = "Some"
  else:
    space = "Plenty"

  print(f"Space available: {space}")

  return False

def main():
  """Main function for Thanksgiving Dinner."""
  print("- Thanksgiving Dinner -")
  print("Serve yourself as much food as you like from the buffet, but make sure that your plate will hold without spilling everywhere!")

  print("Choose a plate:")
  print("1. Small Sturdy Plate")
  print("2. Large Flimsy Plate")
  plate_choice = check_input.get_int_range("Enter choice: ", 1, 2)

  if plate_choice == 1:
    plate = SmallPlate()
  else:
    plate = LargePlate()

  while True:
    print("1. Turkey")
    print("2. Stuffing")
    print("3. Potatoes")
    print("4. Green Beans")
    print("5. Pie")
    print("6. Quit")
    
    food_choice = check_input.get_int_range("Enter choice: ", 1, 6)

    if food_choice == 6:
      print(plate.description())
      print(f"Good job! You made it to the table with {plate.count()} items.")
      print(f"There was still {plate.area()} square inches of space left on your plate.")
      print(f"Your plate could have held {plate.weight()} more ounces of food.")
      print("Don't worry, you can always go back for more. Happy Thanksgiving!")
      break

    if food_choice == 1:
      plate = Turkey(plate)
    elif food_choice == 2:
      plate = Stuffing(plate)
    elif food_choice == 3:
      plate = Potatoes(plate)
    elif food_choice == 4:
      plate = GreenBeans(plate)
    elif food_choice == 5:
      plate = Pie(plate)

    if examine_plate(plate):
      break
main()