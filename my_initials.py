import turtle

wn = turtle.Screen()
wn.bgcolor("white")

henok = turtle.Turtle()
henok.shape("turtle")
henok.color("blue")
henok.speed(5)

henok.right(90)
henok.forward(100)
henok.right(180)
henok.forward(50)
henok.right(90)
henok.forward(50)
henok.left(90)
henok.forward(50)
henok.right(180)
henok.forward(100)

henok.penup()
henok.goto (80, 0)
henok.pendown()

henok.right(1800)
henok.forward(100)
henok.right(180)
henok.forward(50)
henok.right(90)
henok.forward(50)
henok.left(90)
henok.forward(50)
henok.right(180)
henok.forward(100)

wn.exitonclick()