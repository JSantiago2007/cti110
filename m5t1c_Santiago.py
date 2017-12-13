# CTI 110
# M5T1c: Snowflake
# Juan Santiago
# 10/19/2017

import turtle

myPen = turtle.Turtle() #Sets up Turtle
myPen.shape("turtle")
myPen.pensize(6)

myPen.color("blue")

myPen.left(90)


for i in range(0,6): #Makes the snowflake
  myPen.forward(100)
  myPen.forward(-40)
  myPen.left(40)
  myPen.forward(30)
  myPen.forward(-30)
  myPen.right(80)
  myPen.forward(30)
  myPen.forward(-30)
  myPen.left(40)
  myPen.forward(-60)

  myPen.right(60)












   





