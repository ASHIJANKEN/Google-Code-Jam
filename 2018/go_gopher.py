import sys

cells = [[False for i in range(1000)] for j in range(1000)]
min_pos = [1000, 1000]
max_pos = [0, 0]
desig_row = 0
desig_col = 0

def count_frontier(pos):
  frontier = 0
  for i in range(3):
    for j in range(3):
      if cells[pos[0]-1+i][pos[1]-1+j] == False:
        frontier += 1
  return frontier

def is_rectangle():
  next_pos = []
  next_pos_canditate = []
  max_frontier = 0
  min = [int(500 - desig_row/2), 500 - int(desig_col/2)]
  max = [int(500 + desig_row/2), 500 + int(desig_col/2)]
  for i in range(min[0],  max[0]+1):
    for j in range(min[1], max[1]+1):
      if cells[i][j] == False:
        next_pos_canditate = [i, j]
        if next_pos_canditate[0] == min[0]:
          next_pos_canditate[0] += 1
        if next_pos_canditate[0] == max[0]:
          next_pos_canditate[0] -= 1
        if next_pos_canditate[1] == min[1]:
          next_pos_canditate[1] += 1
        if next_pos_canditate[1] == max[1]:
          next_pos_canditate[1] -= 1

        frontier = count_frontier(next_pos_canditate)
        if frontier > max_frontier:
          next_pos = next_pos_canditate
          max_frontier = frontier
  
  return next_pos

def determine_next_pos(require_cell):
  if cells[require_cell[0]][require_cell[1]] == False:
    return require_cell
  return is_rectangle()

t = int(input('')) # read a line with a single integer

for case in range(t):

  # Initialize values
  cells = [[False for i in range(1000)] for j in range(1000)]
  require_cell = [500, 500]
  min_pos = [1000, 1000]
  max_pos = [0, 0]

  a = int(input(''))

  if a == 20:
    desig_col = 5
    desig_row = 4
  elif a == 200:
    desig_col = 50
    desig_row = 40

  print(str(require_cell[0]) + " " + str(require_cell[1]), flush=True)

  while True:
    prepared = input('')
    prepared =  [int(s) for s in prepared.split(" ")]

    if prepared == [-1, -1]:
      sys.exit(1)
    elif prepared == [0, 0]:
      break;
    else:
      cells[prepared[0]][prepared[1]] = True

    require_cell = determine_next_pos(require_cell)
    print(str(require_cell[0]) + " " + str(require_cell[1]), flush=True)


[[False, True, False, False, True],
[True, False, False, True, False],
[False, False, False, False, False],
[False, False, True, False, False],
[False, False, False, False, False],]