import turtle
stamp = turtle.Turtle()
stamp.shape("turtle")

stamp.color("orange")

stamp.penup()
for i in range (5):
    stamp.forward(50)
    stamp.stamp()
