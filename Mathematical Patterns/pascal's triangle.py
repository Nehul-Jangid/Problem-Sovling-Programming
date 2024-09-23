height = 5
triangle = [[1]]
# index = 0

for row in range(1,height):

  new_row = [1]
  for i in range(1,row):
    new_row.append(triangle[row-1][i-1] + triangle[row-1][i])

  new_row.append(1)
  triangle.append(new_row)
  # print(triangle)
  
 

 
for row in triangle:
  space = height - len(row)
  print(" "*space, end="")
  print(" ".join(map(str, row)))



  