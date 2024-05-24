full_brick = "|___"
half_brick = "|_"

height = int(input())
width = int(input())

if height % 2 == 0:
  height1 = int(height / 2)
  height2 = True
else:
  height2 = False
  height1 = int((height / 2)-0.5)

print("_"*(width*4+1))

def row1():
  for i in range(width):
     print(full_brick, end="")
  print("|")

def row2():
  print(half_brick, end="")
  for i in range(width-1):
    print(full_brick, end="")
  print(half_brick, end="")
  print("|")

if height1 == 1:
  row1()
  row2()
else:
  for i in range(height1):
    row1()
    row2()

if height2 == False:
    row1()
elif height2 == True:
    print("")
