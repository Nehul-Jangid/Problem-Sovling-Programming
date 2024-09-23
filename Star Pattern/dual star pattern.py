# Goal:
#     *  *
#    **  ** 
#   ***  ***
#  ****  ****
# *****  *****

height = 5 #Height of the pattern
space = 0 # space variable for printing in the first pattern
for row in range(height):
  space = height - row - 1 # Calculating spaces ex. height = 10 row = 5, spaces will be 10 - 5 - 1 = 4
  print(" "* space, end ="") # printing space for left side pattern
  for char in range(row + 1 ): # left pattern loop, row + 1 so that the first row does'nt remain empty else the row will start from 0 
    print(f"*",end="")
  print("  ", end="") # Middle space
  for char in range(row + 1): # right pattern loop
    print(f"*",end="")
  print() # new line