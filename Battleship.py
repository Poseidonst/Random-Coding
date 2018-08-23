from random import randint

board = []

for x in range(4):
  board.append(["O"] * 4)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)


for turn in range(16):
    print ("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
      print ("Congratulations! You sunk my battleship!")
      print ("You have guessed it in " +str(turn +1)+" times!")
      break
    else:
      if guess_row not in range(len(board)) or guess_col not in range(len(board)):
        print ("Oops, that's not even in the ocean.")
      elif(board[guess_row][guess_col] == "X"):
        print ("You guessed that one already.")
      else:
        print ("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        if turn == 15:
          print ("Game Over, the battleship was placed here:")
          board[ship_row][ship_col] = "H"
      print_board(board)
