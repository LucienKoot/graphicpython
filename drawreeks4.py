#for loop stamp

import turtle
stam = turtle.Turtle()
stam.shape("turtle")

stam.penup()

for a in ["orange", "cyan","green"]:
    stam.color(a)
    stam.forward(50)
    stam.stamp()
