import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

# version 1
tim.shape("turtle")
tim.color("blue")

for _ in range(3):
  tim.pencolor("black")
  tim.forward(10)
  tim.pencolor('white')
  tim.forward(10)

# version 2
#tim.shape("turtle")
tim.color("blue")

for _ in range(15):
  tim.forward(10)
  tim.penup()
  tim.forward(10)
  tim.pendown()
