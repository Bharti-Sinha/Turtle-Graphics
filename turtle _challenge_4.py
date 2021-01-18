import turtle as t
import random

tim = t.Turtle()

# ########## Challenge 4 - Random Walk ########

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
turn = [0, 90, 180, 270]
tim.pensize(5)
tim.speed('fastest')

for _ in range(200):
    tim.color(random.choice(colours))
    tim.left(random.choice(turn))
    tim.forward(30)
    tim.setheading(random.choice(turn))
