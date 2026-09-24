from turtle import *
step = 100

color("orange")
forward(100)

forward(step)
color("red")
left(90)
forward(100)

color("green")
left(90)
forward(100)

color("blue")
left(90)
forward(100)


reset()

letter_size = 30
gap = 10

penup()

backward_length = (letter_size * 2) + (gap * 2)
backward(backward_length)


pendown()
left(90)
forward(letter_size * 2)
backward(letter_size)
right(90)
forward(letter_size)
left(90)
forward(letter_size)
backward(letter_size * 2)
right(90)
penup()
forward(gap)


pendown()
left(90)
forward(letter_size)
right(90)
forward(letter_size)
right(90)
forward(letter_size / 2)
right(90)
forward(letter_size)
left(90)
forward(letter_size / 2)
left(90)
forward(letter_size)
penup()
forward(gap)


pendown()
left(90)
forward(letter_size * 2)
backward(letter_size * 2)
right(90)
penup()
forward(gap)


pendown()
left(90)
forward(letter_size * 2)
backward(letter_size * 2)
right(90)
penup()
forward(gap)


pendown()
forward(letter_size)
left(90)
forward(letter_size)
left(90)
forward(letter_size)
left(90)
forward(letter_size)
left(90)
penup()
forward(gap)

done()