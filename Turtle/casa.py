import turtle

t = turtle.Turtle()
t.shape('blank')
x = 100

#retangulo inicial
t.fillcolor('white smoke')
t.begin_fill()
for _ in range(2):
	t.forward(2*x)
	t.left(90)
	t.forward(x)
	t.left(90)
t.end_fill()

t.forward(x/3)
t.left(90)

#porta
t.fillcolor('saddle brown')
t.begin_fill()
for _ in range(2):
	t.forward(2*x/3)
	t.right(90)
	t.forward(x/3)
	t.right(90)
t.end_fill()

t.right(90)
t.forward(x/3 + x/4)
t.left(90)
t.up()
t.forward(x/3)
t.down()

#janela esquerda
t.fillcolor('light cyan')
t.begin_fill()
for _ in range(4):
	t.forward(x/3)
	t.right(90)
t.end_fill()

t.right(90)
t.up()
t.forward(x/3 + x/4)
t.left(90)
t.down()

#janela direita
t.fillcolor('light cyan')
t.begin_fill()
for _ in range(4):
	t.forward(x/3)
	t.right(90)
t.end_fill()

t.up()
t.forward(2*x/3)
t.right(90)
t.forward(x/2)
t.left(135)
t.down()

#telhado
t.fillcolor('peru')
t.begin_fill()
t.forward(x*(2**(1/2)))
t.left(90)
t.forward(x*(2**(1/2)))
t.left(135)
t.forward(2*x)
t.end_fill()

#beiral direito
t.right(45)
t.forward(x/4)
t.right(180)
t.forward(x/4)

t.left(45)
t.forward(2*x)

#beiral direito
t.left(45)
t.forward(x/4)
t.right(180)
t.forward(x/4)

turtle.done()