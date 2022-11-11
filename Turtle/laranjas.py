import turtle

t = turtle.Turtle()
t.speed(50)

t.fillcolor('orange')
t.up()

razao = 50
for raio in range(10, 200, razao):
	t.begin_fill()
	t.circle(raio)
	t.end_fill()
	t.forward((((2*raio+razao)**2) - (razao**2))**(1/2))
t.down()

turtle.done()