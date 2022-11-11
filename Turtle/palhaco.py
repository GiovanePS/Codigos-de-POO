import turtle

t = turtle.Turtle()
t.speed(50)

t.left(90)
#olhos
for _ in range(2):
	t.begin_fill()
	t.circle(25)
	t.end_fill()
	t.color('blue')
	for raio in range(50, 100+1, 25):
		t.circle(raio)
	t.color('black')
	t.right(180)

t.up()
t.right(180)
t.forward(150)
t.color('magenta')
t.down()
#nariz
for angulo in range(0, 360, 5):
	t.forward(50)
	t.left(180)
	t.forward(50)
	t.left(180)
	t.left(5)

t.color('red')
t.width(10)
t.up()
t.right(45)
t.forward(100)
t.left(90)
t.down()
#boca
t.circle(100, 90)
	
turtle.done()