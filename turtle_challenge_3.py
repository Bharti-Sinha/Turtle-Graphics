import turtle as t
import random

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########
colors = ['red', 'yellow', 'blue', 'green', 'beige']
for n_sides in range(3,11):
  tim.color(random.choice(colors))
  angle = 360/n_sides
  for _ in range(0,n_sides):
    tim.forward(100) 
    tim.right(angle)


