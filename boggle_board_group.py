import random
import time
class BoggleBoard:
  dice = [
    ['AAEEGN','ELRTTY','AOOTTW','ABBJOO',],
    ['EHRTVW','CIMOTU','DISTTY','EIOSST',],
    ['DELRVY','ACHOPS','HIMNQU','EEINSU',],
    ['EEGHNW','AFFKPS','HLNNRZ','DEILRX',]
  ]
  
  
  def __init__(self):
    print('\nWelcome to Boggle Board!')
    for i in range(4):
      print('________')

    input('\nPress enter to shake the board!: ')

    while True:
      Terminal.clear()
      BoggleBoard.shake()
      choice = input('\nPress "Q" to quit or "enter" to shake the board: >>')
      if choice == 'q':
        print('\n Exiting the game.....')
        time.sleep(1)
        break

  
  @classmethod
  def shake(cls):
    for group in cls.dice:
      row = ''
      for die in group:
        num = random.randint(0,5)
        if die[num] == 'Q':
          row += 'Qu '
        else:
          row += die[num] + '  '
      print(row)
    
class Terminal:
    @staticmethod
    def clear():
        print("\033c", end="")
    
      

# Board = BoggleBoard()

BoggleBoard()