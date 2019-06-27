#for loop stamp
import turtle

mijnstempel = turtle.Turtle()

mijnstempel.shape("turtle")

mijnstempel.penup()

for i in ["orange", "cyan","purple"]:
    mijnstempel.color(i)
    mijnstempel.forward(50)
    mijnstempel.stamp()
