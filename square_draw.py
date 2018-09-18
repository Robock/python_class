import turtle
def draurtle(some_turtle):
	for i in range (1,5):
		some_turtle.forward(40)
		some_turtle.right(90)

	
	

def flwr():
	wind = turtle.Screen()
	wind.bgcolor("yellow")
	
	tom = turtle.Turtle()
	tom.shape("turtle")
	tom.color("green")
	tom.speed(0)
	rotation_angle = 10
	full_circle = 360
	while rotation_angle < full_circle:
		draurtle(tom)
		tom.right(rotation_angle)
		rotation_angle=rotation_angle+10
	tom.right(270)
	tom.forward(100)

	wind.exitonclick()

flwr()

'''def flwr():
	wind = turtle.Screen()
	wind.bgcolor("white")
	
	tom = turtle.Turtle()
	tom.shape("turtle")
	tom.color("green")
	tom.speed(0)

	clrs = ["yellow", "red", "purple", "blue"]
	for c in clrs:
		tom.color(c)
		tom.forward(50)
		tom.left(90)

	wind.exitonclick()
	
flwr()'''