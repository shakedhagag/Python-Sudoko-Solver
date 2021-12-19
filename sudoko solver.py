
board=[[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],
[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],
[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9]]
#------------------------------------------------------------------------  
#print pretty
#------------------------------------------------------------------------  
def print_board(board):
  if board is None:
    print("Empty Board")
  col = len(board[0])
  row = len(board)
  print("         SODUKO    ")
  for i in range(row):
    line_to_print=""
    if i%3 == 0:
      print("-------------------------")
    for j in range(col):
      if board[i][j] == 0:
        board[i][j] = ' '
      if j%3 ==0:
        line_to_print +="| " + str(board[i][j]) + " "
      else:
        line_to_print += str(board[i][j]) + " "
    print(line_to_print + "|")
  print("-------------------------")



#------------------------------------------------------------------------  
## Print the Soduko board
#------------------------------------------------------------------------  
def printboard(board):
  if board is None:
    print("Empty Board")
  col = len(board[0])
  row = len(board)
  for i in range(row):
    line_to_print=""
    for j in range(col):
      line_to_print += str(board[i][j]) + ", "
    print(line_to_print)    

#------------------------------------------------------------------------  
## Find the indexes of the empty cells (Empty cells contain 0)
#------------------------------------------------------------------------  
def findzero(board):
  zero_ans = []
  for i in board:
  
      if 0 in i:
        zero_ans.append(board.index(i))
        zero_ans.append(i.index(0))
        return zero_ans
      else:
        None
#------------------------------------------------------------------------      
# Check if a value is valid in the empty cell according to soduko rules
#------------------------------------------------------------------------  
def isvalid(board, row, col, value):
  #Check row
  if value in board[row]:
   return False
  #Check column
  for i in board:
   if i[col] == value:
     return False
 #Divide the soduko board to 3X3 boards
  x=(row//3)*3
  y=(col//3)*3

  for j in range(0,3):
    for k in range(0,3):
      if board[x+j][y+k]==value:
        return False
  return True
    
#------------------------------------------------------------------------  
#Solve the soduko board using recursion
#------------------------------------------------------------------------  
def solve(board):
  zPlacement = findzero(board)
  #Base Case
  if zPlacement == None:
    return print_board(board)
  x = zPlacement[0]
  y = zPlacement[1]  
  #recursive case
  for i in range(1, 10):
     if isvalid(board, x, y, i):
       board[x][y] = i
       solve(board)
       board[x][y] = 0
   
  return None

solve(board)