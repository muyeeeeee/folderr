#triangle
import turtle
t = turtle.Turtle()

#subprogramtodrawatriangle
def drawtriangle():
  for i in range(3):
    t.forward(100)
    t.left(120)
    
drawtriangle()

#rectangle
import turtle
t = turtle.Turtle()

#subprogramtodrawarectangle
def drawrectangle():
  for i in range(2):
    t.forward(100)
    t.right(90)
    t.forward(50)
    t.right(90)
drawrectangle()

#circle
import turtle
t = turtle.Turtle()

#subprogramtodrawacircle
def drawcircle():
  t.circle(50)
  
drawcircle()

#diamond
import turtle
t = turtle.Turtle()

#subprogramtodrawadiamond
def drawdiamond():
  t.forward(100)
  t.right(45)
  t.forward(100)
  t.right(135)
  t.forward(100)
  t.right(45)
  t.forward(100)
  
drawdiamond()

#square
import turtle
t = turtle.Turtle()

#subprogramtodrawasquare
def drawsquare():
  for i in range(4): 
    t.forward(100)
    t.right(90)
  
drawsquare()
