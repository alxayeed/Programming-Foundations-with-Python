#Drawing a circle from a Square

import turtle

def draw_SquareCircle():
	sc = turtle.Turtle()
	sc.speed(50)
	sc.color('red')

	window = turtle.Screen()
	window.bgcolor('white')

	for i in range(360):
		sc.forward(100)
		sc.right(90)
		sc.forward(100)
		sc.right(90)
		sc.forward(100)
		sc.right(90)
		sc.forward(100)
		sc.right(91)



	window.exitonclick()


draw_SquareCircle()