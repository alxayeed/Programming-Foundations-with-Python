#Drawing a circle from a Square

import turtle

#function to draw a circle from drawing squares
def draw_SquareCircle():
	sc = turtle.Turtle()
	sc.speed(50)
	sc.color('red')

	window = turtle.Screen()
	window.bgcolor('white')
	
	#inner function that will draw square
	def draw_square():
		for side in range(4):
			sc.forward(100)
			sc.right(90)

	#drawing a square for 180 times with 2 degree angle
	for i in range(180):
		draw_square()
		sc.right(2)



	window.exitonclick()


draw_SquareCircle()