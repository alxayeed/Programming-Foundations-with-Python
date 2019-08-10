#Drawing a flower using rectangle 

import turtle

#Function that will draw the flower
def draw_flower():
	fl = turtle.Turtle()
	fl.speed(30)
	fl.shape('turtle')
	fl.color('cyan')

	window = turtle.Screen()
	window.bgcolor('white')

	fl.left(90)
	fl.forward(250)

	#Inner function that will draw rectangle 
	def draw_ractangle():
		fl.right(30)
		fl.forward(70)
		fl.right(30)
		fl.forward(70)
		fl.right(150)
		fl.forward(70)
		fl.right(30)
		fl.forward(70)

	#Drawing the rectangle for 75 times
	for i in range(75):
		draw_ractangle()
		fl.right(5)

	window.exitonclick()

draw_flower()