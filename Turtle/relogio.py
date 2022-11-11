import turtle

t = turtle.Turtle()
t.shape('blank')
t.speed(50)
t.width(3)

t.circle(100)
t.left(90)
t.up()
t.forward(10)
t.right(90)
for _ in range(12):
    t.circle(90, 30)
    t.dot(5)

t.left(90)
t.forward(90)
t.down()

#ponteiro maior preto
t.right(85)
t.forward(75)
t.left(180)
t.forward(75)

#ponteiro menor preto
t.right(40)
t.width(5)
t.forward(50)
t.left(180)
t.forward(50)
t.width(3)

#ponteiro vermelho
t.color('red')
t.width(2)
t.left(130)
t.forward(88)
t.left(180)
t.forward(88)

turtle.done()