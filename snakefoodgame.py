import turtle
import random

def getrandommodule():
 import turtle
 import random

def setturtle():
 # Set the Turtle Screen for the game
 turtle.setup(400,500)
 wn = turtle.Screen() 
 wn.title("Handling keypresses!") 
 wn.bgcolor("lightgreen")

def createsnake():
 turt = turtle.Turtle() 
 turt.shape("arrow")
 turt.color("black")
 turt.penup()
 turt.goto(0,100)
 turt.pensize(7)
 turt.pendown()
 return turt

def createsnakefood():
 food = turtle.Turtle()
 food.speed(0)
 food.shape("circle")
 food.color("red")
 food.penup()
 food.shapesize(0.50, 0.50)
 food.goto(0, 0)
 return food

def randomization():
 z=random.randint(-200,200)
 return z

def turtleup(tess):
  return tess.forward(30)

def turtleleft(tess):
  return tess.left(45)

def turtleright(tess):
  return tess.right(45)

def turtleback(tess):
  return tess.backward(30) 

def turtlequit(tess):
  #print("bye")
  #tess.penup()
  return tess.hideturtle()

def gamerules():
  print("****Rules of the Game****")
  print("The two main characters of this game are:\n- The Snake(Black Arrow)\n- The food(red circle)")
  print("The player has to move the snake such that it eats(touches) the food.")
  print("The players uses the arrow keys to move and turn")
  print("The player gets 10 points if the snake eats the food")
  print("Click the snake(black arrow) and use the arrow keys to start playing")