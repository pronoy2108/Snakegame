# Snake will move around and eat the food. 
# Everytime it eats the food, you score
# Let's code the game


'''Activity 1: Wake Up the Snake '''
# To save you some time, and let Python do some hard work for you and let's lift the code
# Uncomment the statements below 

import turtle
import snakefoodgame

print("Uncomment the statements below and give a name to the snake and food in the placeholder")

''' Ensure you use the same name for the snake and the food throughout the program'''

#Place the names inside the placeholder (<  >)

snakefoodgame.gamerules()
snakefoodgame.getrandommodule()
snakefoodgame.setturtle()
#<student to provide snake name>=snakefoodgame.createsnake()
#<student to provide snake food name>=snakefoodgame.createsnakefood()

'''Activity 2: Define Snake movement functions '''
# Uncomment the statements below to:
# - Set the score to 0
# - Get your snake moving by providing the name of your snake

##Set the score 
score=0
##Function to set snake movement
def snakeup():
#  <student to provide snake name>.forward(30)
def snakeleft():
#  <student to provide snake name>.left(45)
def snakeright():
#  <student to provide snake name>.right(45)
def snakeback():
#  <student to provide snake name>.backward(30) 


'''Activity 3: Set the game window '''
# Uncomment the statement below to set the game window.
# Pick a colour from Red, Blue, Green

wn = turtle.Screen() 
wn.bgcolor("<Choose Red, Blue or Green>") 
#<student to provide snake name>.penup()

'''Activity 4: Bind arrow keys'''
# The final task is to get the snake to eat the food 
# And you get a score :)
# Continue to score as the food moves to a random location 
# To keep the game going, lets use a loop 
# Uncomment the statements below and provide values in the placeholder to complete the final task.


#while True:
  wn.update()
  wn.onkey(snakeup, "Up")
  wn.onkey(snakeleft, "Left")
  wn.onkey(snakeright, "Right")
  wn.onkey(snakeback, "Down")
  wn.listen() 
##Check if the snake ate the food
  if <student to provide snake name>.distance(<student to provide snake food name>)<20 :
    x=snakefoodgame.randomization()
    y=snakefoodgame.randomization()    
    <student to provide snake food name>.goto(x, y)
    score=score+10
    print("Score: ",score)
    wn.mainloop()    

# Your game is ready. Click Run to start the game 

'''Awesome!! You have created a lovely game'''