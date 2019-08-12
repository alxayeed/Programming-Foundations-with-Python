#Drawing a sqaure
import turtle

def draw_art():
	window =turtle.Screen()
	window.bgcolor('blue')

	#Drawing Square
	squere = turtle.Turtle() #creating object of class turtle from module turtle
	squere.color('white')
	squere.shape('turtle')
	squere.speed(1)

	for side in range(4):
		squere.forward(150)
		squere.right(90)

	#Drawing Triangle
	circ = turtle.Turtle()
	circ.color('yellow')
	circ.shape('turtle')
	circ.circle(100)


	#Drawing Triangle
	tr = turtle.Turtle()
	tr.color('green')
	tr.shape('turtle')
	
	for side in range(3):
		tr.forward(100)
		tr.left(120)

	window.exitonclick()


draw_art()
