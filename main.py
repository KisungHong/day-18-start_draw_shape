# import turtle
# tim = turtle.Turtle()
import random
from turtle import Turtle, Screen
import heroes

tim = Turtle()
tim.shape("turtle")
tim.color("blue", "red")


# for sketch in range(30):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


colours = ["blue", "red", "black"]



def draw_shape(num_sides):
    angle = 360 / num_sides
    tim.color(random.choice(colours))
    for sketch in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
