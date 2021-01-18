import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed('fastest')


# ########## Challenge 5 - Spirograph ########


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(gap):
    for _ in range(int(360 / gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading() + gap
        tim.setheading(current_heading)


draw_spirograph(5)
my_screen = t.Screen()
my_screen.exitonclick()
