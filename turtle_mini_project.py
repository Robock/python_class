import turtle

def colorful_square(some_turtle):

	tri_colors = ["red", "green", "blue"]

	for i in tri_colors:
		some_turtle.color(i)
		some_turtle.forward(100)
		some_turtle.right(120)

def initials(henok):
	henok.right(180)
	henok.forward(100)
	henok.right(180)
	henok.forward(50)
	henok.left(90)
	henok.forward(50)
	henok.left(90)
	henok.forward(50)
	henok.right(180)
	henok.forward(100)

	henok.penup()
	henok.goto (180, -260)
	henok.pendown()

	henok.right(180)
	henok.forward(100)
	henok.right(180)
	henok.forward(50)
	henok.left(90)
	henok.forward(50)
	henok.left(90)
	henok.forward(50)
	henok.right(180)
	henok.forward(100)

def triangular_flower():
	wn = turtle.Screen()
	wn.bgcolor("white")

	henok = turtle.Turtle()
	henok.shape("turtle")
	henok.speed(10)
	henok.color("black")

	rotation_angle = 5
	full_rotation = 360

	for i in range (0,full_rotation,rotation_angle):
		colorful_square(henok)
		henok.right(rotation_angle)

	henok.right(90)
	henok.forward(250)

	henok.penup()
	henok.goto (110, -260)
	henok.pendown()
	initials(henok)

	'''henok.right(180)
	henok.forward(100)
	henok.right(180)
	henok.forward(50)
	henok.left(90)
	henok.forward(50)
	henok.left(90)
	henok.forward(50)
	henok.right(180)
	henok.forward(100)

	henok.penup()
	henok.goto (180, -260)
	henok.pendown()

	henok.right(180)
	henok.forward(100)
	henok.right(180)
	henok.forward(50)
	henok.left(90)
	henok.forward(50)
	henok.left(90)
	henok.forward(50)
	henok.right(180)
	henok.forward(100)'''

	wn.exitonclick()

triangular_flower()