import random
import turtle
from turtle import Turtle, Screen
import colorgram

turtle.colormode(255)   # allows to randomly choose different colors


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


directions = [0, 90, 180, 270]



timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("darkblue")

timmy_the_turtle.speed('fastest')
timmy_the_turtle.pensize(10)


for _ in range(200):
    timmy_the_turtle.color(random_color())      # using random colors
    # timmy_the_turtle.speed(random.randint(1, 11))
    # timmy_the_turtle.pensize(random.randint(5, 15))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))



screen = Screen()
screen.exitonclick()

