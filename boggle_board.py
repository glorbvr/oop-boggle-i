import random

class BoggleBoard:

  def __init__(self):
    self.rows = []
    self.row1 = ["_" for x in range (0,4)]
    self.row2 = ["_" for x in range (0,4)]
    self.row3 = ["_" for x in range (0,4)]
    self.row4 = ["_" for x in range (0,4)]
    self.rows.append(self.row1)
    self.rows.append(self.row2)
    self.rows.append(self.row3)
    self.rows.append(self.row4)

    for i in self.rows:
      print(i)

  def shake(self):
    # random.shuffle(dice.dice_cube)
    # Dice.roll_dice(self)
    pass

class Dice:
  
  def __init__(self):
    self.dice_cube = list("""AAEEGN
ELRTTY
AOOTTW
ABBJOO
EHRTVW
CIMOTU
DISTTY
EIOSST
DELRVY
ACHOPS
HIMNQU
EEINSU
EEGHNW
AFFKPS
HLNNRZ
DEILRX""".split())
  
    for i, dice in enumerate(self.dice_cube):
      self.dice_cube[i] = [letter for letter in self.dice_cube[i]]
  
  def roll_dice(self):
    for i in self.dice_cube:
      random.shuffle(i)
      return i[0]

board = BoggleBoard()
dice = Dice()

print(dice.roll_dice())
board.shake()
# print(dice.dice_cube)
# random.shuffle(dice.dice_cube)
# print(dice.dice_cube)
