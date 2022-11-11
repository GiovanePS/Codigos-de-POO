import turtle
from math import pi

t = turtle.Turtle()
t.speed(100)
raio = 70

t.width(5)
t.right(90)
t.forward(200)
t.left(180)
t.width(1)
t.forward(50)
t.right(90)
for _ in range(2):
	t.circle(30, 90)
	t.left(90)
t.left(90)
t.forward(150)
t.left(7.5)
for y in range(7):
	for x in range(2):
		t.circle(raio, 90)
		t.left(90)
	t.left(360/7)

turtle.done()