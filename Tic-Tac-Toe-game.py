import turtle

#Using turtle to draw board
def drawgrid(mypen):
  mypen.color("orange")
  mypen.begin_fill()
  mypen.penup()
  mypen.goto(-1.0 / 2, 0)
  mypen.penup()
  mypen.goto(-150, 150)
  mypen.pendown()

  mypen.goto(150, 150)
  mypen.goto(150, -150)
  mypen.goto(-150, -150)
  mypen.goto(-150, 150)

  mypen.end_fill()

  mypen.pensize(6)
  mypen.color("light blue")

  mypen.penup()

  mypen.goto(50, 0)

  mypen.pendown()

  mypen.left(90)
  mypen.forward(150)
  mypen.right(180)
  mypen.forward(300)

  mypen.penup()

  mypen.goto(-50, 0)

  mypen.pendown()

  mypen.forward(150)
  mypen.right(180)
  mypen.forward(300)

  mypen.penup()

  mypen.goto(0, -50)

  mypen.pendown()

  mypen.left(90)
  mypen.forward(150)
  mypen.right(180)
  mypen.forward(300)

  mypen.penup()

  mypen.goto(0, 50)

  mypen.pendown()

  mypen.forward(150)
  mypen.right(180)
  mypen.forward(300)


#------------------------------------------------------------
#Using turtle to write players and their symbols
def drawletter(mypen):
  mypen.penup()

  mypen.goto(-150, -175)

  mypen.color("Black")
  style = ("Comic Sans MS", 10, "bold")
  mypen.write("Player-1: X", font=style, align="left")
  #----------------------------------------------------------
  mypen.goto(65, -175)

  mypen.color("Black")
  style = ("Comic Sans MS", 10, "bold")
  mypen.write("Player-2: O", font=style, align="left")


#------------------------------------------------------------
  #Numbers to see in grid
def drawnumber(mypen):
  mypen.penup()
  for i in range(3):
    mypen.goto(-145 + 100 * i, 130)
    mypen.color("Black")
    style = ("Comic Sans MS", 10, "bold")
    mypen.write(i + 1, font=style, align="left")
    mypen.penup()
#------------------------------------------------------------
  for j in range(3):
    mypen.goto(-145 + 100 * j, 30)
    mypen.color("Black")
    style = ("Comic Sans MS", 10, "bold")
    mypen.write(j + 4, font=style, align="left")
    mypen.penup()
#------------------------------------------------------------
  for k in range(3):
    mypen.goto(-145 + 100 * k, -70)
    mypen.color("Black")
    style = ("Comic Sans MS", 10, "bold")
    mypen.write(k + 7, font=style, align="left")
    mypen.penup()


#------------------------------------------------------------
  #To draw symbol after user inputs number like X or O
def drawsymbol(pos, sym):
  if pos == 1:
    mypen.goto(-100, 30)
    mypen.color("dark blue")
    style = ("Arial", 85, "normal")
    mypen.write(sym, font=style, align="center")
#------------------------------------------------------------
  if pos == 2:
    mypen.goto(0, 30)
    mypen.color("dark blue")
    style = ("Arial", 85, "normal")
    mypen.write(sym, font=style, align="center")
#------------------------------------------------------------
  if pos == 3:
    mypen.goto(100, 30)
    mypen.color("dark blue")
    style = ("Arial", 85, "normal")
    mypen.write(sym, font=style, align="center")
#------------------------------------------------------------
  if pos == 4:
    mypen.goto(-100, -70)
    mypen.color("dark blue")
    style = ("Arial", 85, "normal")
    mypen.write(sym, font=style, align="center")
#------------------------------------------------------------
  if pos == 5:
    mypen.goto(0, -70)
    mypen.color("dark blue")
    style = ("Arial", 85, "normal")
    mypen.write(sym, font=style, align="center")
#------------------------------------------------------------
  if pos == 6:
    mypen.goto(100, -70)
    mypen.color("dark blue")
    style = ("Arial", 85, "normal")
    mypen.write(sym, font=style, align="center")
#------------------------------------------------------------
  if pos == 7:
    mypen.goto(-100, -170)
    mypen.color("dark blue")
    style = ("Arial", 85, "normal")
    mypen.write(sym, font=style, align="center")
#------------------------------------------------------------
  if pos == 8:
    mypen.goto(0, -170)
    mypen.color("dark blue")
    style = ("Arial", 85, "normal")
    mypen.write(sym, font=style, align="center")
#------------------------------------------------------------
  if pos == 9:
    mypen.goto(100, -170)
    mypen.color("dark blue")
    style = ("Arial", 85, "normal")
    mypen.write(sym, font=style, align="center")

#To check who won

def Checkwin():
  if gameboard[0] == gameboard[1] == gameboard[2] != "_":
    mypen.penup()
    mypen.color("green")
    mypen.goto(-130,100)
    mypen.pendown()
    mypen.goto(130,100)
    if gameboard[0] == "X":
      print("Player-1 wins!!!")
      return True

    elif gameboard[0] == "O":
      print("Player-2 wins!!!")
      return True


  if gameboard[3] == gameboard[4] == gameboard[5] != "_":
    mypen.penup()
    mypen.color("green")
    mypen.goto(-130,0)
    mypen.pendown()
    mypen.goto(130,0)
    if gameboard[3] == "X":
      print("Player-1 wins!!!")
      return True

    elif gameboard[3] == "O":
      print("Player-2 wins!!!")
      return True

  if gameboard[6] == gameboard[7] == gameboard[8] != "_":
    mypen.penup()
    mypen.color("green")
    mypen.goto(-130,-100)
    mypen.pendown()
    mypen.goto(130,-100)
    if gameboard[6] == "X":
      print("Player-1 wins!!!")
      return True

    elif gameboard[6] == "O":
      print("Player-2 wins!!!")
      return True

  if gameboard[0] == gameboard[4] == gameboard[8] != "_":
    mypen.penup()
    mypen.color("green")
    mypen.goto(-140,140)
    mypen.pendown()
    mypen.goto(140,-140)
    if gameboard[0] == "X":
      print("Player-1 wins!!!")
      return True

    elif gameboard[0] == "O":
      print("Player-2 wins!!!")
      return True

  if gameboard[0] == gameboard[3] == gameboard[6] != "_":
    mypen.penup()
    mypen.color("green")
    mypen.goto(-100,140)
    mypen.pendown()
    mypen.goto(-100,-140)
    if gameboard[0] == "X":
      print("Player-1 wins!!!")
      return True

    elif gameboard[0] == "O":
      print("Player-2 wins!!!")
      return True

  if gameboard[2] == gameboard[5] == gameboard[8] != "_":
    mypen.penup()
    mypen.color("green")
    mypen.goto(100,140)
    mypen.pendown()
    mypen.goto(100,-140)
    if gameboard[2] == "X":
      print("Player-1 wins!!!")
      return True

    elif gameboard[2] == "O":
      print("Player-2 wins!!!")
    return True

  if gameboard[1] == gameboard[4] == gameboard[7] != "_":
    mypen.penup()
    mypen.color("green")
    mypen.goto(0,140)
    mypen.pendown()
    mypen.goto(0,-140)
    if gameboard[0] == "X":
      print("Player-1 wins!!!")
      return True

    elif gameboard[0] == "O":
      print("Player-2 wins!!!")
      return True

  if gameboard[2] == gameboard[4] == gameboard[6] != "_":
    mypen.penup()
    mypen.color("green")
    mypen.goto(100,140)
    mypen.pendown()
    mypen.goto(-100,-140)
    if gameboard[2] == "X":
      print("Player-1 wins!!!")
      return True

    elif gameboard[2] == "O":
      print("Player-2 wins!!!")
      return True

  return False

#main programe---------------------------------------------
myscreen = turtle.Screen()
myscreen.setup(1.0, 1.0)
myscreen.bgcolor("White")

mypen = turtle.Turtle()
mypen.color("light blue")
drawgrid(mypen)
drawnumber(mypen)
drawletter(mypen)

positionlist = []
gameboard = ["_","_","_","_","_","_","_","_","_"]
currentPlayer = 1

#User to input position
while True:
  while True:
    try:
      position = input("Enter position (1-9): ")
      position = int(position)

      if position >= 1 and position <= 9 and position not in positionlist:
        if currentPlayer == 1:
          drawsymbol(position, "X")
          gameboard[position - 1] = "X"
          currentPlayer = 2
        else:
          drawsymbol(position, "O")
          gameboard[position - 1] = "O"
          currentPlayer = 1

        positionlist.append(position)

        break
      else:
        print("Invalid entry. Please try again")

    except:
      print("Invalid entry. Please try again")

  result = Checkwin()
  if result == True:
    break
#To check if game tied
  if "_" not in gameboard:
    print("It's a tie!!!")
    break
input()
